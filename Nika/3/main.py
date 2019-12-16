import xml.dom.minidom
from dataxml import dataxml

parser = dataxml("/Users/glebnazemnov/Documents/#main/#WORK/sgu /4/oop/practice/Nika/3/data.xml")
parser.parseData()
parser.writeData()
parser.writeDb("newDb.sqlite")
