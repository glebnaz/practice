from typeOfCredit import types
from client import client
from credit import credit
from dataWorker import dataWorker

parser = dataWorker("data.xml")
parser.parse()
parser.writeXml()
