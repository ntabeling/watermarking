# Photo Watermarking
### Watermark images using python 3 and the PIL library
### Dependencies
* Python 3.8.2
* Pillow 8.3.0

### Configs
* `/configs/abbreviations.json` - Dictionary of stormwater feature abbreviations. Do Not Modify This File.
* `/configs/paths.json`
    - incsv: Location of the `PhotoInfo.csv` file that contains the information to be watermarked.
    - problemfiles: Location and name of a text file that will be created to list files that did not watermark successfully.
    - imgin: Location of the directory where the imgs to be located are stored. As delivered this directory should contain a number of subdirectories that will be unpacked to access the individual files as part of the watermarking process. You will not need to unpack the subdirectories manually.
    - imgout: Path to the directory where watermarked images will be saved.
* `/configs/watermark.json` - As configured, the watermarker will apply two watermarks to each image; a date in the upper left of the image and some notes about the image centered at the bottom of the image. X and Y are a percentages of the total height and width of the image to be watermarked with (0,0) being the upper left hand corner of the image.\\If there is a need to change the location of either watermark the process of adjusting the coordinates is largely trial and error to get the new watermark dialed in. To adjust the locations change the X and Y values for "TOP" and "BOTTOM" in the config to be the new (X,Y) values of the watermark, relative to the upper left (0,0)

### Note about running the watermarker task
When the task is run on MacOS a .DS_Store file is created that is causing the task to fail on the first run. It needs to
be deleted before the task is run again. Working to find a permanent resolution