from utils import wmDictCreator, fixOrientation, createWatermark

def watermarkPhotos():
    ImageFile.LOAD_TRUNCATED_IMAGES = True

    config = './configs/template.json'
    with open(config,"r") as x:
        config = json.load(x)

    files = wmDictCreator(config['incsv'])

    problemfiles = open(config['problemfiles'], 'w')

    fixOrientation()

    for k, v in files.items():
        if os.path.isfile(config['imgin'] + k):
            copyfile(os.path.join(config['imgin'],k), os.path.join(config['imgout'],k))
            for key, val in files[k].items():
                createWatermark(k, key, val[0], val[1], val[2])
        else:
            problemfiles.write(f'{k}\n')

if __name__ == "__main__":
    watermarkPhotos()