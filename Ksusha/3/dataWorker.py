import xml.dom.minidom
from typeOfCredit import types
from client import client
from credit import credit
import sqlite3 as db

emptydb = """
PRAGMA foreign_keys = ON;

create table type_of_credit
(id integer primary key,
name text,
conditional text,
rate text,
term text);

create table client
(id integer primary key,
name text,
adress text,
phone text,
person text);


create table credits
(id integer primary key autoincrement,
type_of_credit integer references type_of_credit(id) on update cascade on delete cascade,
client integer references client(id) on update cascade on delete cascade,
data text,
cost text,
unique(type_of_credit,client))"""


class dataWorker:
    def __init__(self,filename=""):
        self.filename = filename
        self.clientsList = dict()
        self.creditList = dict()
        self.typeOfCreditsList = dict()

    def parseClient(self):
        doc = xml.dom.minidom.parse(self.filename)
        clients = doc.getElementsByTagName("client")
        for Client in clients:
            id = Client.getAttribute("id")
            name = Client.getAttribute("name")
            typeOfProperty = Client.getAttribute("typeOfProperty")
            adress = Client.getAttribute("adress")
            phone = Client.getAttribute("phone")
            person = Client.getAttribute("person")
            newClient = client(name,typeOfProperty,adress,phone,person)
            newClient.setId(id)
            self.clientsList[id] = newClient
        print(self.clientsList)

    def writeDb(self,out):
        conn = db.connect(out)
        curs = conn.cursor()
        curs.executescript(emptydb) #if you start at first time
        self.parseXml()
         #write clients
        for clientsId in self.clientsList:
            clients = self.clientsList[clientsId]
            curs.execute("insert into client(id,name,adress,phone,person)values('%s','%s','%s','%s','%s')"%(
             clientsId,
             clients.getName(),
             clients.getAdress(),
             clients.getPhone(),
             clients.getPerson()))
        for typeOfCreditId in self.typeOfCreditsList:
            typeOfCredit = self.typeOfCreditsList[typeOfCreditId]
            curs.execute("insert into type_of_credit(id,name,conditional,rate,term)values('%s','%s','%s','%s','%s')"%(
            str(typeOfCreditId),
            str(typeOfCredit.getName()),
            str(typeOfCredit.getConditional()),
            str(typeOfCredit.getRate()),
            str(typeOfCredit.getTerm())))
        for creditId in self.creditList:
            credit = self.creditList[creditId]
            curs.execute("insert into credits(id,type_of_credit,client,data,cost)values('%s','%s','%s','%s','%s')"%(
            str(creditId),
            str(credit.getTypeOfCredit().getId()),
            str(credit.getClient().getId()),
            str(credit.getData()),
            str(credit.getCost())))
        conn.commit()
        conn.close()

    def readDb(self,inp):
        conn = db.connect(inp)
        curs = conn.cursor()
        curs.execute('select * from client')
        data=curs.fetchall()
        for r in data:print(r)
        curs.execute('select * from type_of_credit')
        data=curs.fetchall()
        for r in data:print(r)
        curs.execute('select * from credits')
        data=curs.fetchall()
        for r in data:print(r)
        conn.close()

    def parseTypeOfCredit(self):
        doc = xml.dom.minidom.parse(self.filename)
        typeOfCredits = doc.getElementsByTagName("typeOfCredit")
        for TypeOfCredit in typeOfCredits:
            id = TypeOfCredit.getAttribute("id")
            name = TypeOfCredit.getAttribute("name")
            conditional = TypeOfCredit.getAttribute("conditional")
            rate = TypeOfCredit.getAttribute("rate")
            term = TypeOfCredit.getAttribute("term")
            newtypeOfCredit = types(name,conditional,rate,term)
            newtypeOfCredit.setId(id)
            self.typeOfCreditsList[id] = newtypeOfCredit
        print(self.typeOfCreditsList)
    def parseCredit(self):
        doc = xml.dom.minidom.parse(self.filename)
        credits = doc.getElementsByTagName("credit")
        for Credit in credits:
            id = Credit.getAttribute("id")
            clientId = Credit.getAttribute("client")
            typeOfCreditId = Credit.getAttribute("typeOfCredit")
            data = Credit.getAttribute("data")
            cost = Credit.getAttribute("cost")
            client = self.clientsList[clientId]
            typeOfCredit = self.typeOfCreditsList[typeOfCreditId]
            newCredit = credit(typeOfCredit,client,data,cost)
            newCredit.setId(id)
            self.creditList[id] = newCredit
        print(self.creditList)

    def writeXml(self):
        doc = xml.dom.minidom.Document()
        root = doc.createElement('bank')
        doc.appendChild(root)
        clients = doc.createElement("clients")
        for clientId in self.clientsList:
            client = self.clientsList[clientId]
            clientXml = doc.createElement("client")
            clientXml.setAttribute('name', client.getName())
            clientXml.setAttribute('typeOfProperty', client.getTypeOfProperty())
            clientXml.setAttribute('adress', client.getAdress())
            clientXml.setAttribute('phone', client.getPhone())
            clientXml.setAttribute('person', client.getPerson())
            clients.appendChild(clientXml)
        root.appendChild(clients)
        typeOfCredits = doc.createElement("typeOfCredits")
        for typeOfCreditId in self.typeOfCreditsList:
            typeOfCredit = self.typeOfCreditsList[typeOfCreditId]
            typeOfCreditXml = doc.createElement("typeOfCredit")
            typeOfCreditXml.setAttribute('name', typeOfCredit.getName())
            typeOfCreditXml.setAttribute('conditional', typeOfCredit.getConditional())
            typeOfCreditXml.setAttribute('rate', typeOfCredit.getRate())
            typeOfCreditXml.setAttribute('term', typeOfCredit.getTerm())
            typeOfCredits.appendChild(typeOfCreditXml)
        root.appendChild(typeOfCredits)
        credits = doc.createElement("credits")
        for creditId in self.creditList:
            credit = self.creditList[creditId]
            creditXml = doc.createElement("credit")
            creditXml.setAttribute("data",credit.getData())
            creditXml.setAttribute("cost",credit.getCost())
            typeOfCredit = credit.getTypeOfCredit()
            typeOfCreditXmlcredit = doc.createElement("typeOfCredit")
            typeOfCreditXmlcredit.setAttribute('name', typeOfCredit.getName())
            typeOfCreditXmlcredit.setAttribute('conditional', typeOfCredit.getConditional())
            typeOfCreditXmlcredit.setAttribute('rate', typeOfCredit.getRate())
            typeOfCreditXmlcredit.setAttribute('term', typeOfCredit.getTerm())
            creditXml.appendChild(typeOfCreditXmlcredit)
            client = credit.getClient()
            patientXmlcredit = doc.createElement("client")
            patientXmlcredit.setAttribute('name', client.getName())
            patientXmlcredit.setAttribute('typeOfProperty', client.getTypeOfProperty())
            patientXmlcredit.setAttribute('adress', client.getAdress())
            patientXmlcredit.setAttribute('phone', client.getPhone())
            patientXmlcredit.setAttribute('person', client.getPerson())
            creditXml.appendChild(patientXmlcredit)
            credits.appendChild(creditXml)
        root.appendChild(credits)
        xml_str = doc.toprettyxml(indent="  ")
        with open("new.xml", "w") as f:
            f.write(xml_str)
    def parseXml(self):
        self.parseClient()
        self.parseTypeOfCredit()
        self.parseCredit()
