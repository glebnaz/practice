import xml.dom.minidom
from dataxml import dataxml

parser = dataxml("data.xml")
parser.parseData()
parser.writeData()
parser.writeDb("newDb.sqlite")
