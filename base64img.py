#!/usr/bin/env python
import base64
import sys
import mimetypes

if len(sys.argv) < 2: 
	sys.exit("Usage: " + sys.argv[0] + " inputfile [html | css | url]")
filename = sys.argv[1]

mime = mimetypes.guess_type(filename)[0]
prepend = ""
append = ""

if len(sys.argv) > 2: 
	lang = sys.argv[2]
	if lang == "html":
		prepend = "<img alt=\"\" src=\"data:" + mime + ";base64,"
		append = "\" />"
	elif lang == "css":
		prepend = "background-image: url(\"data:" + mime + ";base64,"
		append = "\");"
	elif lang == "url":
		prepend = "\"data:" + mime + ";base64,"
		append = "\""

with open(filename, "rb") as image_file:
    print prepend + base64.b64encode(image_file.read()) + append
