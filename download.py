#!/usr/bin/env python

import urllib, gzip, os

file = "epg.xml.gz"
outfilename= "epg.xml"
url = "http://epg.kodibg.org/dl.php"

#Download
urllib.urlretrieve(url, file)

#Extract
inF = gzip.open(file, 'rb')
outF = open(outfilename, 'wb')
outF.write( inF.read() )
inF.close()
outF.close()

#remove zip
os.remove(file)
