import json
from datetime import datetime
import csv
import os
import shutil
from PIL import Image, ExifTags, ImageDraw, ImageFont

def wm_dict_creator(table):
    toWatermark = {}
    
    abbrevs = "/Users/ntabeling/repos/watermarking/configs/abbreviations.json"
    with open(abbrevs,"r") as x:
        abbrevs = json.load(x)

    wmConfig = "/Users/ntabeling/repos/watermarking/configs/watermark.json"
    with open(wmConfig,"r") as x:
        wmConfig = json.load(x)

    with open(table, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            date = datetime.strptime(row[0].strip(".jpg")[-8:],"%Y%m%d").strftime("%m/%d/%Y")
            if row[5] == "":
                watermark = f"BMP {row[1]} - {abbrevs[row[4]]}"
            else:
                watermark = f"BMP {row[1]} - {abbrevs[row[4]]} - {row[5]}"
            toWatermark[row[0]] = {
                "top": [
                    date,
                    float(wmConfig["TOP"]["X"]),
                    float(wmConfig["TOP"]["Y"])
                ],
                "bottom": [
                    watermark,
                    float(wmConfig["BOTTOM"]["X"]),
                    float(wmConfig["BOTTOM"]["Y"])
                ]
            }
    return toWatermark

def unpack_dirs():
    config = "/Users/ntabeling/repos/watermarking/configs/paths.json"
    with open(config,"r") as x:
        config = json.load(x)

    indir = config["imgin"]
    for x in os.listdir(indir):
        if os.path.isdir(os.path.join(indir,x)):
            p = os.path.join(indir,x)
            for y in os.listdir(p):
                src = os.path.join(p,y)
                dst = os.path.join(indir,y)
                shutil.copy(src, dst)

def fix_orientation():
    config = "/Users/ntabeling/repos/watermarking/configs/paths.json"
    with open(config,"r") as x:
        config = json.load(x)

    for photo in os.listdir(config["imgin"]):
        if os.path.isfile(os.path.join(config["imgin"],photo)) and photo[-4:] != ".csv":
            try:
                image = Image.open(os.path.join(config["imgin"], photo))
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation] == "Orientation":
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
                # cases: image don"t have getexif
                pass

def create_watermark(filename, position, watermark, xmod, ymod):
    config = "/Users/ntabeling/repos/watermarking/configs/paths.json"
    with open(config,"r") as x:
        config = json.load(x)
    
    text = watermark
    color = "white"
    fontfamily = "/System/Library/Fonts/Supplemental/arial.ttf"
    image = Image.open(os.path.join(config["imgout"],filename)).convert("RGBA")
    imageWatermark = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(imageWatermark)
    width, height = image.size
    font = ImageFont.truetype(fontfamily, int(height / 20))
    textWidth, textHeight = draw.textsize(text, font)
    if position == "bottom":
        x = (width - textWidth)/2
        y = height * ymod
        box = [x, y, (x+textWidth), (y+textHeight)]
    else:
        x = width * xmod
        y = height * ymod
        box = [x, y, (x+textWidth), (y+textHeight)]
    draw.rectangle(box, fill="black", outline="black", width=0)
    draw.text((x, y), text, color, font)
    wmImg = Image.alpha_composite(image, imageWatermark)
    wmImg.convert("RGB").save(filename)
