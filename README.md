base64img.py
============

A script to encode image files as base64 text. 

Usage
--
 
    ./base64img.py inputfile [html | css | url]

If no second parameter is passed then the raw base64 encoded text is outputted to the terminal. If `url` is passed, then the text will be formatted as a data url and wrapped in double quotes (e.g. `"data:image/png;base64,iVBORw0KGgoAAAANSUhE"`). If `html` or `css` is passed, then the data url will additionally be wrapped in the appropriate markup (either `url()` for css or `<image />` for html). 
