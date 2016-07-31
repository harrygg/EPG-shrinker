import re

xml = open("epg.xml", 'r').read()
m = re.compile(">(.+?)</display").findall(xml)
print "%s ids found" % len(m)

ids = open("all_channel_ids.txt", "w")
for i in range (0, len(m)):
  ids.write(m[i] + '\n')
ids.close()
