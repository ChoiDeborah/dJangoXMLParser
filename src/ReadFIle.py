# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

path = "/Users/deborah/Desktop/dJangoXMLParser/xml/Hero - Mariah Carey.xml"


f = open(path, 'r')
string = ""
isline = False

while True:
    line = f.readline()
    if not line:
        break
    if not line == '\n' and not line[:4] == '<!--':
        string += line
        isline = True
    else:
        if isline:
            isline = False

    if not isline:
        if not string == "":
            root = ET.fromstring(string)
            print(root.tag)
            string = ""
            isline = False

f.close()


# for child in root:
#    print child.tag, child.attrib
