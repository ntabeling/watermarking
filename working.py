import csv
import configparser
from PIL import Image, ImageDraw, ImageFont

config = configparser.ConfigParser()
config.read('config.ini')

'''
draw.text is where the watermark gets applied. Need to find a way to perform
that function three times - one for each watermark.

The x and y variables probably need to be set within a dict so they can be
associated with an individual watermark.
'''


def watermark_image_with_text(filename, watermark):
    text = watermark
    color = 'blue'
    fontfamily = 'arial.ttf'
    image = Image.open(config['PATHS']['imgIn'] + filename).convert('RGBA')
    imageWatermark = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(imageWatermark)
    width, height = image.size
    font = ImageFont.truetype(fontfamily, int(height / 20))
    textWidth, textHeight = draw.textsize(text, font)
    x = width * .5
    y = height * .95
    draw.text((x, y), text, color, font)
    my_img = Image.alpha_composite(image, imageWatermark)
    my_img.convert('RGB').save(config['PATHS']['imgOut'] + 'water_' + filename)
    return config['PATHS']['imgOut'] + 'water_' + filename


with open(config['PATHS']['inCSV']) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        watermarktext = row[1:4]
        print(config['PATHS']['imgIn'] + row[0])
        watermark_image_with_text(row[0], row[1])
