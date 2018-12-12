# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

path = "/Users/deborah/Desktop/dJangoXMLParser/xml/test.xml"


#print(note)


f = open(path, 'r')
string = '';


while True:
    line = f.readline()
    if not line: break
    string += line;
    #print(line)
f.close()


#print(string)


tree = ET.parse(path)
root = tree.getroot()

root = ET.fromstring(string)

print(root.tag)
#print(root.attrib)

#for child in root:
#    print child.tag, child.attrib

for neighbor in root.iter():
    print neighbor.attrib

