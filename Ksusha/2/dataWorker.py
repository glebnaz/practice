import xml.dom.minidom
from typeOfCredit import types
from client import client
from credit import credit
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
            self.clientsList[id] = newClient
        print(self.clientsList)


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
        file = "new"+self.filename
        with open("new.xml", "w") as f:
            f.write(xml_str)

    def addCredit(self,credit,id):
        self.creditList[id]=credit
        print("add new credit")

    def addClient(self,client,id):
        self.clientsList[id]=client
        print("add new client")

    def addTypeOfCredit(self,type,id):
        self.typeOfCreditsList[id]=type
        print("add new type of recdit")

    def delCredit(self,id):
        del self.creditList[id]

    def delClient(self,id):
        del self.clientsList[id]

    def delTypeOfCredit(self,id):
        del self.typeOfCreditsList[id]

    def parse(self):
        self.parseClient()
        self.parseTypeOfCredit()
        self.parseCredit()
