# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from typing import Any, Union

path = "/Users/deborah/Desktop/dJangoXMLParser/example/Example_Sentences_181216.xml"
global count
global totalCount
totalCount = 0

def Load_XML(pathName):
    f = open(pathName, 'r')
    string = ""
    isline = False
    count = 0


    while True:
        line = f.readline()
        if not line:
            if not isline:
                break



        if not line == '\n' and not line[:4] == '<!--' and not line == '':
            string += line
            isline = True
        else:
            if isline:
                isline = False

        if not isline and not string == "":
            root = ET.fromstring(string)
            print(count+1)
            print(root.tag)

            string = ""
            count += 1
            isline = False

    f.close()
    return count


for i in range(1, 13):

    print(i)
    totalCount += Load_XML("/Users/deborah/Desktop/dJangoXMLParser/xml/"+str(i)+".xml")

    print(totalCount)
