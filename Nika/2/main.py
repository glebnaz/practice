import xml.dom.minidom
from dataxml import dataxml

parser = dataxml("2/data.xml")

parser.parseData()
parser.writeData()
