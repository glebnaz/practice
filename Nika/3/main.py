import xml.dom.minidom
from dataxml import dataxml

parser = dataxml("data.xml")

parser.writeDb("newDb.sqlite")
