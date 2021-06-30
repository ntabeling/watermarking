import json
from datetime import datetime
import csv

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
