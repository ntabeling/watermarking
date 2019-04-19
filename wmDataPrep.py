import configparser
import csv
from datetime import datetime


def wmDictCreator(table):
    wmConfig = configparser.ConfigParser()
    wmConfig.read('./configs/wm-location-config.ini')
    toWatermark = {}
    abbrevs = {
        'ACC': 'Access of Habitation',
        'CS': 'Control Structure',
        'EMB': 'Embankment',
        'ES': 'Emergency Spillway',
        'ERO': 'Erosion',
        'HAB': 'Evidence Blocked',
        'FEN': 'Fence',
        'FOR': 'Forebay',
        'HAZ': 'Hazards',
        'ILL': 'Ilicit Discharges',
        'INF': 'Inflow',
        'LOW': 'Low Flow Orifice',
        'MOT': 'Maintenance of Traffic',
        'MAJ': 'Major Outfalls',
        'OBW': 'Observation Well',
        'OTH': 'Other Maintenance Items',
        'OUT': 'Outfall',
        'OV': 'Overall',
        'RIS': 'Riser',
        'WER': 'Weir'
    }
    with open(table) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            datestring = row[0].strip('.jpg')[-8:]
            date = datetime.strptime(datestring, '%Y%m%d').strftime('%m/%d/%Y')
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
