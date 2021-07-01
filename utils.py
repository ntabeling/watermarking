import json
from datetime import datetime
import csv
import os
from PIL import Image, ExifTags

def wmDictCreator(table):
    toWatermark = {}
    
    abbrevs = "./configs/abbreviations.json"
    with open(abbrevs,"r") as x:
        abbrevs = json.load(x)

    wmConfig = "./configs/watermark.json"
    with open(wmConfig,"r") as x:
        wmConfig = json.load(x)

    with open(table, encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            datestring = row[0].strip('.jpg')[-8:]
            date = datetime.strptime(datestring, '%Y%m%d').strftime('%m/%d/%Y')
            if row[5] == "":
                watermark = f"BMP {row[1]} - {abbrevs[row[4]]}"
            else:
                watermark = f"BMP {row[1]} - {abbrevs[row[4]]} - {row[5]}"
            toWatermark[row[0]] = {
                'top': [
                    date,
                    float(wmConfig['TOP']['X']),
                    float(wmConfig['TOP']['Y'])
                ],
                'bottom': [
                    watermark,
                    float(wmConfig['BOTTOM']['X']),
                    float(wmConfig['BOTTOM']['Y'])
                ]
            }
    return toWatermark

def fixOrientation():
    config = configparser.ConfigParser()
    config.read('./configs/config.ini')

    config = './configs/template.json'
    with open(config,"r") as x:
        config = json.load(x)

    for photo in os.listdir(config['imgin']):
        try:
            image = Image.open(os.path.join(config['imgin'], photo))
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = dict(image._getexif().items())

            if exif[orientation] == 3:
                image = image.rotate(180, expand=True)
                image.save(photo)
            elif exif[orientation] == 6:
                image = image.rotate(270, expand=True)
                image.save(photo)
            elif exif[orientation] == 8:
                image = image.rotate(90, expand=True)
                image.save(photo)
            image.close()

        except (AttributeError, KeyError, IndexError):
            # cases: image don't have getexif
            pass
