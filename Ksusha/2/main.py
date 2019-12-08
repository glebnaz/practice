from typeOfCredit import types
from client import client
from credit import credit
from dataWorker import dataWorker

parser = dataWorker("2/data.xml")
parser.parse()
parser.writeXml()
