import xml.dom.minidom
from actor import actor
from performances import performances
from labor import labor
import sqlite3 as db

emptydb = """
PRAGMA foreign_keys = ON;

create table actor
(id integer primary key,
first_name text,
last_name text,
father_name text,
rank text,
experience text);

create table performance
(id integer primary key,
name text,
year text,
budget text);


create table labor
(id integer primary key autoincrement,
actor integer references actor(id) on update cascade on delete cascade,
performance integer references performance(id) on update cascade on delete cascade,
role text,
cost text,
unique(actor,performance))"""
class dataWorker:
    def __init__(self,filename=""):
        self.filename = filename
        self.actorsList = dict()
        self.laborList = dict()
        self.performansessList = dict()


    def writeDb(self,out):
        conn = db.connect(out)
        curs = conn.cursor()
        curs.executescript(emptydb) #if you start at first time
        self.parseXml()
        #write performances
        for performancesId in self.performansessList:
            performances = self.performansessList[performancesId]
            curs.execute("insert into performance(id,name,year,budget)values('%s','%s','%s','%s')"%(
            performancesId,
            performances.getName(),
            performances.getyear(),
            performances.getbudget()))
        for actorId in self.actorsList:
            actor = self.actorsList[actorId]
            curs.execute("insert into actor(id,first_name,last_name,father_name,rank,experience)values('%s','%s','%s','%s','%s','%s')"%(
            str(actorId),
            str(actor.getfirstName()),
            str(actor.getlastName()),
            str(actor.getfatherName()),
            str(actor.getrank()),
            str(actor.getexperience())))
        for laborId in self.laborList:
            labor = self.laborList[laborId]
            curs.execute("insert into labor(id,actor,performance,role,cost)values('%s','%s','%s','%s','%s')"%(
            str(laborId),
            str(labor.getactor().getId()),
            str(labor.getperformances().getId()),
            str(labor.getrole()),
            str(labor.getCost())))
        conn.commit()
        conn.close()

    def parseActor(self):
        doc = xml.dom.minidom.parse(self.filename)
        actors = doc.getElementsByTagName("actor")
        for Actor in actors:
            id = Actor.getAttribute("id")
            firstName = Actor.getAttribute("firstName")
            lastName = Actor.getAttribute("lastName")
            fatherName = Actor.getAttribute("fatherName")
            rank = Actor.getAttribute("rank")
            expirience = Actor.getAttribute("expirience")
            newActor = actor(firstName,lastName,fatherName,rank,expirience)
            newActor.setId(id)
            self.actorsList[id] = newActor
        print(self.actorsList)


    def parsePerformanses(self):
        doc = xml.dom.minidom.parse(self.filename)
        performansess = doc.getElementsByTagName("performances")
        for Performanses in performansess:
            id = Performanses.getAttribute("id")
            name = Performanses.getAttribute("name")
            year = Performanses.getAttribute("year")
            budget = Performanses.getAttribute("budget")
            newperformanses = performances(name,year,budget)
            newperformanses.setId(id)
            self.performansessList[id] = newperformanses
        print(self.performansessList)

    def parseLabor(self):
        doc = xml.dom.minidom.parse(self.filename)
        labors = doc.getElementsByTagName("labor")
        for Labor in labors:
            id = Labor.getAttribute("id")
            actorId = Labor.getAttribute("actor")
            performansesId = Labor.getAttribute("performances")
            data = Labor.getAttribute("role")
            cost = Labor.getAttribute("cost")
            actor = self.actorsList[actorId]
            performanses = self.performansessList[performansesId]
            newlabor = labor(actor,performanses,data,cost)
            newlabor.setId(id)
            self.laborList[id] = newlabor
        print(self.laborList)

    def writeXml(self):
        doc = xml.dom.minidom.Document()
        root = doc.createElement('bank')
        doc.appendChild(root)
        actors = doc.createElement("actors")
        for actorId in self.actorsList:
            actor = self.actorsList[actorId]
            actorXml = doc.createElement("actor")
            actorXml.setAttribute('firstName', actor.getfirstName())
            actorXml.setAttribute('lastName', actor.getlastName())
            actorXml.setAttribute('fatherName', actor.getfatherName())
            actorXml.setAttribute('rank', actor.getrank())
            actorXml.setAttribute('experience', actor.getexperience())
            actors.appendChild(actorXml)
        root.appendChild(actors)
        performansess = doc.createElement("performances")
        for performansesId in self.performansessList:
            performanses = self.performansessList[performansesId]
            performansesXml = doc.createElement("performance")
            performansesXml.setAttribute('name', performanses.getName())
            performansesXml.setAttribute('year', performanses.getyear())
            performansesXml.setAttribute('budget', performanses.getbudget())
            performansess.appendChild(performansesXml)
        root.appendChild(performansess)
        labors = doc.createElement("labors")
        for laborId in self.laborList:
            labor = self.laborList[laborId]
            laborXml = doc.createElement("labor")
            laborXml.setAttribute("role",labor.getrole())
            laborXml.setAttribute("cost",labor.getCost())
            performanses = labor.getperformances()
            performansesXmllabor = doc.createElement("performanses")
            performansesXmllabor.setAttribute('name', performanses.getName())
            performansesXmllabor.setAttribute('year', performanses.getyear())
            performansesXmllabor.setAttribute('budget', performanses.getbudget())
            laborXml.appendChild(performansesXmllabor)
            actor = labor.getactor()
            patientXmllabor = doc.createElement("actor")
            patientXmllabor.setAttribute('firstName', actor.getfirstName())
            patientXmllabor.setAttribute('lastName', actor.getlastName())
            patientXmllabor.setAttribute('fatherName', actor.getfatherName())
            patientXmllabor.setAttribute('rank', actor.getrank())
            patientXmllabor.setAttribute('expirience', actor.getexperience())
            laborXml.appendChild(patientXmllabor)
            labors.appendChild(laborXml)
        root.appendChild(labors)
        xml_str = doc.toprettyxml(indent="  ")
        file = "new"+self.filename
        with open("newFile", "w") as f:
            f.write(xml_str)

    def parseXml(self):
        self.parseActor()
        self.parsePerformanses()
        self.parseLabor()
