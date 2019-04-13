import configparser
from PIL import Image, ImageDraw, ImageFont
from wmDataPrep import wmDictCreator

config = configparser.ConfigParser()
config.read('./config.ini')

files = wmDictCreator(config['PATHS']['incsv'])


def createWatermark(filename, watermark, xmod, ymod):
    text = watermark
    color = 'white'
    fontfamily = 'arial.ttf'
    image = Image.open(config['PATHS']['imgIn'] + filename).convert('RGBA')
    imageWatermark = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(imageWatermark)
    width, height = image.size
    font = ImageFont.truetype(fontfamily, int(height / 20))
    textWidth, textHeight = draw.textsize(text, font)
    x = width * xmod
    y = height * ymod
    draw.text((x, y), text, color, font)


def applyWatermark(filename, wm1, wm2):
    image = Image.open(config['PATHS']['imgIn'] + filename).convert('RGBA')
    wmImg = Image.alpha_composite(image, wm1, wm2)
    wmImg.convert('RGB').save(config['PATHS']['imgOut'] + 'water_' + filename)
    return config['PATHS']['imgOut'] + 'water_' + filename
