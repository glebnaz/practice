from actor import actor
from performances import performances
from labor import labor
from dataWorker import dataWorker

parser = dataWorker("2/data.xml")
parser.parse()
parser.writeXml()
