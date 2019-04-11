import configparser
import csv

pathConfig = configparser.ConfigParser()
pathConfig.read('./configs/config.ini')

wmConfig = configparser.ConfigParser()
wmConfig.read('./configs/wm-location-config.ini')

incsv = pathConfig['PATHS']['incsv']

files = {}

with open(incsv) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        files[row[0]] = {
            'top': {
                'wm': row[1],
                'x': float(wmConfig['TOP']['X']),
                'y': float(wmConfig['TOP']['Y'])
            },
            'mid': {
                'wm': row[2],
                'x': float(wmConfig['MID']['X']),
                'y': float(wmConfig['MID']['Y'])
            },
            'bottom': {
                'wm': row[3],
                'x': float(wmConfig['BOTTOM']['X']),
                'y': float(wmConfig['BOTTOM']['Y'])
            }
        }

print(files)
