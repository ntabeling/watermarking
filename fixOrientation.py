'''
This script checks the orientation of the photo based on the EXIF
and flips it to the 'correct' orientation, if necessary.
'''

import os
from PIL import Image, ExifTags
import configparser


def fixOrientation():
    config = configparser.ConfigParser()
    config.read('./configs/config.ini')

    for photo in os.listdir(config['PATHS']['imgin']):
        try:
            image = Image.open(config['PATHS']['imgin'] + photo)
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
