import configparser
import os
from shutil import copyfile
from PIL import Image, ImageDraw, ImageFont
from wmDataPrep import wmDictCreator
from fixOrientation import fixOrientation

ImageFile.LOAD_TRUNCATED_IMAGES = True

# Create Watermark function - should be broken out.
def createWatermark(filename, position, watermark, xmod, ymod):
    text = watermark
    color = 'white'
    fontfamily = 'arial.ttf'
    image = Image.open(config['PATHS']['imgout'] + filename).convert('RGBA')
    imageWatermark = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(imageWatermark)
    width, height = image.size
    font = ImageFont.truetype(fontfamily, int(height / 20))
    textWidth, textHeight = draw.textsize(text, font)
    if position == 'bottom':
        x = (width - textWidth)/2
        y = height * ymod
        box = [x, y, (x+textWidth), (y+textHeight)]
    else:
        x = width * xmod
        y = height * ymod
        box = [x, y, (x+textWidth), (y+textHeight)]
    draw.rectangle(box, fill='black', outline='black', width=0)
    draw.text((x, y), text, color, font)
    wmImg = Image.alpha_composite(image, imageWatermark)
    wmImg.convert('RGB').save(config['PATHS']['imgOut'] + filename)


# Set configs
config = configparser.ConfigParser()
config.read('./configs/config.ini')

# Prepare necessary data structure using data prep function
files = wmDictCreator(config['PATHS']['incsv'])

# Set variable for problem files
problemfiles = open(config['PATHS']['problemfiles'], 'w')

# Flip photo orientations
fixOrientation()

# Watermark the photos
for k, v in files.items():
    if os.path.isfile(config['PATHS']['imgin'] + k):
        copyfile(config['PATHS']['imgin'] + k, config['PATHS']['imgout'] + k)
        for key, val in files[k].items():
            createWatermark(k, key, val[0], val[1], val[2])
    else:
        problemfiles.write(f'{k}\n')
