import xml.dom.minidom
import sqlite3 as db
from client import client
from auto import auto
from case import case

class dataWorker:
    def __init__(self,filename=""):
        self.filename = filename
        self.clientsList = dict()
        self.casesList = dict()
        self.autosList = dict()

    def parseClient(self):
        doc = xml.dom.minidom.parse(self.filename)
        clients = doc.getElementsByTagName("client")
        for Client in clients:
            id = Client.getAttribute("id")
            firstName = Client.getAttribute("firstName")
            lastName = Client.getAttribute("lastName")
            fatherName = Client.getAttribute("fatherName")
            adress = Client.getAttribute("adress")
            phone = Client.getAttribute("phone")
            newclient = client(firstName,lastName,fatherName,adress,phone)
            newclient.setId(id)
            self.clientsList[id] = newclient
        print(self.clientsList)

    def parseAuto(self):
        doc = xml.dom.minidom.parse(self.filename)
        autos = doc.getElementsByTagName("auto")
        for Auto in autos:
            id = Auto.getAttribute("id")
            mark = Auto.getAttribute("mark")
            cost = Auto.getAttribute("cost")
            case_cost = Auto.getAttribute("case_cost")
            typ = Auto.getAttribute("typ")
            newauto = auto(mark,cost,case_cost,typ)
            newauto.setId(id)
            self.autosList[id] = newauto
        print(self.autosList)

    def parseCase(self):
        doc = xml.dom.minidom.parse(self.filename)
        labors = doc.getElementsByTagName("case")
        for Case in labors:
            id = Case.getAttribute("id")
            autoId = Case.getAttribute("auto")
            clientId = Case.getAttribute("client")
            dataout = Case.getAttribute("dataout")
            datareturn = Case.getAttribute("datareturn")
            auto = self.autosList[autoId]
            client = self.clientsList[clientId]
            newcase = case(client,auto,dataout,datareturn)
            newcase.setId(id)
            self.casesList[id] = newcase
        print(self.casesList)

    def writeXml(self):
        doc = xml.dom.minidom.Document()
        root = doc.createElement('autopark')
        doc.appendChild(root)
        clients = doc.createElement("clients")
        for clientId in self.clientsList:
            client = self.clientsList[clientId]
            clientXml = doc.createElement("client")
            clientXml.setAttribute('firstName', client.getfirstName())
            clientXml.setAttribute('lastName', client.getlastName())
            clientXml.setAttribute('fatherName', client.getfatherName())
            clientXml.setAttribute('phone', client.getphone())
            clientXml.setAttribute('adress', client.getadress())
            clients.appendChild(clientXml)
        root.appendChild(clients)
        autos = doc.createElement("autos")
        for autoId in self.autosList:
            auto = self.autosList[autoId]
            autoXml = doc.createElement("auto")
            autoXml.setAttribute('name', auto.getmark())
            autoXml.setAttribute('cost', auto.getcost())
            autoXml.setAttribute('case_cost', auto.getcaseCost())
            autoXml.setAttribute('typ', auto.gettyp())
            print("tut")
            print(auto)
            autos.appendChild(autoXml)
        root.appendChild(autos)
        cases = doc.createElement("cases")
        for caseId in self.casesList:
            case = self.casesList[caseId]
            caseXml = doc.createElement("case")
            caseXml.setAttribute("dataout",case.getdateout())
            caseXml.setAttribute("datareturn",case.getdatereturn())
            auto = case.getautos()
            autoXmlcase = doc.createElement("auto")
            autoXmlcase.setAttribute('mark', auto.getmark())
            autoXmlcase.setAttribute('cost', auto.getcost())
            autoXmlcase.setAttribute('case_cost', auto.getcaseCost())
            autoXmlcase.setAttribute('typ', auto.gettyp())
            caseXml.appendChild(autoXmlcase)
            client = case.getclient()
            clientXmlcase = doc.createElement("client")
            clientXmlcase.setAttribute('firstName', client.getfirstName())
            clientXmlcase.setAttribute('lastName', client.getlastName())
            clientXmlcase.setAttribute('fatherName', client.getfatherName())
            clientXmlcase.setAttribute('adress', client.getadress())
            clientXmlcase.setAttribute('phone', client.getphone())
            caseXml.appendChild(clientXmlcase)
            cases.appendChild(caseXml)
        root.appendChild(cases)
        xml_str = doc.toprettyxml(indent="  ")
        file = "new"+self.filename
        with open("newFile", "w") as f:
            f.write(xml_str)



    def parseXml(self):
        self.parseClient()
        self.parseAuto()
        self.parseCase()
