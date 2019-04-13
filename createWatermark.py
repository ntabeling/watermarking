import configparser
from shutil import copyfile
from PIL import Image, ImageDraw, ImageFont
from wmDataPrep import wmDictCreator


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
    else:
        x = width * xmod
        y = height * ymod
    draw.text((x, y), text, color, font)
    wmImg = Image.alpha_composite(image, imageWatermark)
    wmImg.convert('RGB').save(config['PATHS']['imgOut'] + filename)
    return f"{filename}\t{watermark}"


config = configparser.ConfigParser()
config.read('./configs/config.ini')

files = wmDictCreator(config['PATHS']['incsv'])

for k, v in files.items():
    copyfile(config['PATHS']['imgin'] + k, config['PATHS']['imgout'] + k)
    for key, val in files[k].items():
        createWatermark(k, key, val[0], val[1], val[2])
