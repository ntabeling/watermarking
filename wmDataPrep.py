import configparser
import csv
from datetime import datetime


def wmDictCreator(table):
    wmConfig = configparser.ConfigParser()
    wmConfig.read('./configs/wm-location-config.ini')
    watermarks = {}
    abbrevs = {
        'app': 'apple',
        'ora': 'orange'
    }
    with open(table) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            datestring = row[0].strip('.jpg')[-8:]
            date = datetime.strptime(datestring, '%Y%m%d').strftime('%m/%d/%Y')
            watermark = f"BMP {row[1]} - {abbrevs[row[2]]} - {row[3]}"
            watermarks[row[0]] = {
                'top': {
                    'wm': date,
                    'x-mod': float(wmConfig['TOP']['X']),
                    'y-mod': float(wmConfig['TOP']['Y'])
                },
                'bottom': {
                    'wm': watermark,
                    'x-mod': float(wmConfig['BOTTOM']['X']),
                    'y-mod': float(wmConfig['BOTTOM']['Y'])
                }
            }
    return watermarks
