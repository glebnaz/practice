from typeOfCredit import types
from client import client
from credit import credit
from dataWorker import dataWorker

parser = dataWorker("/Users/glebnazemnov/Documents/#main/#WORK/sgu /4/oop/practice/Ksusha/new.xml")
parser.parse()

#пример добавления(для всех остальных классов анологично)
#c = client("Сгу","Государственная","Астраханская 83","500-599","Чумаченко Алексей Николаевич")
#parser.addClient(c,"14")

#пример удаления
#parser.delClient("3")

parser.writeXml()
