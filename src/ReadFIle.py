# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

path = "/Users/deborah/Desktop/dJangoXMLParser/xml/2005 Stanford Commencement Speech - Steve Jobs.xml"


#print(note)


f = open(path, 'r')
string = '';
isline = False

while True:
    line = f.readline()
    if not line: break
    if not line == '\n':
        string += line
        if not isline :
            isline = True

    else:
        if isline:
            if not string == None :
                root = ET.fromstring(string)
                string = ''
                print('\n')
                #if not root == None:
                    #print(root.tag)
                for neighbor in root.iter():
                    if not neighbor == None:
                        print(neighbor.tag, neighbor.attrib)
                isline = False

f.close()





#p

#for child in root:
#    print child.tag, child.attrib



