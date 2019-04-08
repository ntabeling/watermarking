# watermarking

There are some ignored files that contributors will need to create before getting started. In your terminal, navigate to your working directory then run the following commands:
    
`mkdir infolder` - Infolder is the folder where unwatermarked photos go.

`mkdir outfolder` - Outfolder is the folder where photos are dropped after the watermark is applied.


```
touch config.ini
echo "[PATHS]\nincsv = <path/to/csv/ofwatermarks>\nimgin = <path/to/infolder>\nimgout = <path/to/outfolder>" >> config.ini
``` - This config stores relevant paths, like the in and out folders and the path to the csv that will tell the watermarker what to put on each image. After running the command, open config.ini in an editor and modify the paths. Don't forget the quotes.

