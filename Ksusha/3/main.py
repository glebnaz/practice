from typeOfCredit import types
from client import client
from credit import credit
from dataWorker import dataWorker

parser = dataWorker("data.xml")
parser.parseXml()
parser.writeXml()
parser.writeDb("database.sqllite")
parser.readDb("database.sqllite")
