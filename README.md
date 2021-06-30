# Photo Watermarking
### Watermark images using python 3 and the PIL library

There are some ignored files that contributors will need to create before getting started. In your terminal, navigate to your working directory then run the following commands:
    
`mkdir infolder` - Infolder is the folder where unwatermarked photos go.

`mkdir outfolder` - Outfolder is the folder where photos are dropped after the watermark is applied.

`touch config.ini` - Create a config to store useful paths.

`echo "[PATHS]\nincsv = <path/to/csv/ofwatermarks>\nimgin = <path/to/infolder>\nimgout = <path/to/outfolder>" >> config.ini` - This command gets your config in line with mine so we can be working from the same base, without me having to push my actual configs.

### Note about the watermark config
X and Y are a percentage of the total height and width of the image to be watermarked. (0,0) is the upper left hand corner of the image.