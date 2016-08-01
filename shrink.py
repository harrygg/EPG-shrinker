#!/usr/bin/env python                                                                    
import xml.etree.ElementTree as ET
import zipfile, shutil, gzip

included_ids_file = 'IDs.txt'
epg_file = 'epg.xml'
small_epg_file = 'sepg.xml'
small_epg_zip_file = 'sepg.xml.gz'
included_ids = []

#Load the big EPG file
tree = ET.parse(epg_file)
root = tree.getroot()

#Load IDs to be excluded
with open(included_ids_file) as f:
  included_ids = f.read().splitlines()
print "%s channels will be included in the new EGP" % len(included_ids)
#print included_ids

#Remove channel nodes
channels = root.findall('channel')
for c in channels:
  id = c.get('id')
  if id not in included_ids:
    root.remove(c)
    operation = "removed"
  else:
    operation = "added"
  print "Channel %s %s" % (id, operation)

#Remove programme nodes
programmes = root.findall('programme')
for p in programmes:
  if p.get('channel') not in included_ids:
    root.remove(p)

#Write the output file 
tree.write(small_epg_file, 'utf-8', True)   

with open(small_epg_file, 'rb') as f_in, gzip.open(small_epg_zip_file, 'wb') as f_out:
  shutil.copyfileobj(f_in, f_out)