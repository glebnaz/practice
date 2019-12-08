from actor import actor
from performances import performances
from labor import labor
from dataWorker import dataWorker

parser = dataWorker("data.xml")
parser.parseXml()
parser.writeDb("database.sqlite")
parser.readDb("database.sqlite")
