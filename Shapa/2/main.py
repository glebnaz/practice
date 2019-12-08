from actor import actor
from performances import performances
from labor import labor
from dataWorker import dataWorker

parser = dataWorker("data.xml")
parser.parse()
parser.writeXml()
parser.writeDb("database.sqlite")
