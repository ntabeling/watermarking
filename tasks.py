from utils import wm_dict_creator, fix_orientation, create_watermark, unpack_dirs
from PIL import ImageFile
import json

def watermarkPhotos():
    ImageFile.LOAD_TRUNCATED_IMAGES = True

    config = "/Users/ntabeling/repos/watermarking/configs/paths.json"
    with open(config,"r") as x:
        config = json.load(x)

    files = wm_dict_creator(config["incsv"])

    problemfiles = open(config["problemfiles"], "w")

    unpack_dirs()

    fix_orientation()

    for k, v in files.items():
        if os.path.isfile(config["imgin"] + k):
            copyfile(os.path.join(config["imgin"],k), os.path.join(config["imgout"],k))
            for key, val in files[k].items():
                create_watermark(k, key, val[0], val[1], val[2])
        else:
            problemfiles.write(f"{k}\n")

if __name__ == "__main__":
    watermarkPhotos()