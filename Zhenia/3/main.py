from client import client
from auto import auto
from case import case
from dataWorker import dataWorker

c = client("gleb","nazemnov","adnr","moscow","97436395762037")
a = auto("bmw","101202012",1414,"sport")
ca = case(c,a,"22.22.22","22.22.22")

print(c)
print(a)

parser = dataWorker("3/data.xml")
parser.parseXml()
parser.writeXml()
parser.writeDb("newDb.sqllite")
parser.readDb("newDb.sqllite")
