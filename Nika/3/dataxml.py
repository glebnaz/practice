import xml.dom.minidom
from Doctor import Doctor
from Patient import Patient
from Appeal import Appeal
import sqlite3 as db

emptydb = """
PRAGMA foreign_keys = ON;

create table patient
(id integer primary key,
first_name text,
last_name text,
father_name text,
date_of_birth text);

create table doctor
(id integer primary key,
first_name text,
last_name text,
father_name text,
specialty text,
category text);


create table appeal
(id integer primary key autoincrement,
doctor integer references doctor(id) on update cascade on delete cascade,
patient integer references patient(id) on update cascade on delete cascade,
unique(doctor,patient));
"""

class dataxml:
    def __init__(self, filename):
        self.filename = filename
        print(self.filename)
        self.doctorsList = dict()
        self.patientsList = dict()
        self.appealList = dict()



    def writeDb(self,out):
        conn = db.connect(out)
        curs = conn.cursor()
        curs.executescript(emptydb) #if you start at first time
        self.parseData()
        #write patient
        for patientId in self.patientsList:
            patient = self.patientsList[patientId]
            curs.execute("insert into patient(id,first_name,last_name,father_name,date_of_birth)values('%s','%s','%s','%s','%s')"%(
            patientId,
            patient.get_first_name(),
            patient.get_last_name(),
            patient.get_father_name(),
            patient.get_date_of_birth()))
        for doctorId in self.doctorsList:
            doctor = self.doctorsList[doctorId]
            curs.execute("insert into doctor(id,first_name,last_name,father_name,category,specialty)values('%s','%s','%s','%s','%s','%s')"%(
            str(doctorId),
            str(doctor.get_first_name()),
            str(doctor.get_last_name()),
            str(doctor.get_father_name()),
            str(doctor.get_category()),
            doctor.get_specialty()))
        conn.commit()
        conn.close()
    def parseDoctor(self):
        doc = xml.dom.minidom.parse(self.filename)
        doctors = doc.getElementsByTagName("doctor")
        for doctor in doctors:
            id = doctor.getAttribute("id")
            name = doctor.getAttribute("first_name")
            surname = doctor.getAttribute("last_name")
            father_name = doctor.getAttribute("father_name")
            cat = doctor.getAttribute("category")
            sp = doctor.getAttribute("specialty")
            newDoctor = Doctor(name,surname,father_name,cat,sp)
            self.doctorsList[id] = newDoctor
        print("done")    
        print(self.doctorsList)

    def parsePatient(self):
          doc = xml.dom.minidom.parse(self.filename)
          patients = doc.getElementsByTagName("patient")
          for patient in patients:
              id = patient.getAttribute("id")
              name = patient.getAttribute("first_name")
              surname = patient.getAttribute("last_name")
              father_name = patient.getAttribute("father_name")
              date_of_birth = patient.getAttribute("date_of_birth")
              newpatient = Patient(name,surname,father_name,date_of_birth)
              self.patientsList[id] = newpatient
          print(self.patientsList)

    def parseAppeal(self):
        doc = xml.dom.minidom.parse(self.filename)
        appeals = doc.getElementsByTagName("appeal")
        for appeal in appeals:
            id = appeal.getAttribute("id")
            doctorId = appeal.getAttribute("doctor")
            patientId = appeal.getAttribute("patient")
            diagnosis = appeal.getAttribute("diagnosis")
            cost = appeal.getAttribute("cost")
            doctor = self.doctorsList[doctorId]
            patient = self.patientsList[patientId]
            newAppeal = Appeal(doctor,patient,diagnosis,cost)
            self.appealList[id] = newAppeal
        print(self.appealList)

    def parseData(self):
        self.parseDoctor()
        self.parsePatient()
        self.parseAppeal()


    def writeData(self):
        doc = xml.dom.minidom.Document()
        root = doc.createElement('hospital')
        doc.appendChild(root)
        for doctorId in self.doctorsList:
            doctor = self.doctorsList[doctorId]
            doctorXml = doc.createElement("doctor")
            doctorXml.setAttribute('first_name', doctor.get_first_name())
            doctorXml.setAttribute('last_name', doctor.get_last_name())
            doctorXml.setAttribute('father_name', doctor.get_father_name())
            doctorXml.setAttribute('category', doctor.get_category())
            doctorXml.setAttribute('specialty', doctor.get_specialty())
            root.appendChild(doctorXml)
        for patientId in self.patientsList:
            patient = self.patientsList[patientId]
            patientXml = doc.createElement("patient")
            patientXml.setAttribute('first_name', patient.get_first_name())
            patientXml.setAttribute('last_name', patient.get_last_name())
            patientXml.setAttribute('father_name', patient.get_father_name())
            patientXml.setAttribute('date_of_birth', patient.get_date_of_birth())
            root.appendChild(patientXml)
        for appealId in self.appealList:
            appeal = self.appealList[appealId]
            appealXml = doc.createElement("appeal")
            doctor = appeal.get_Doctor()
            doctorXmlAppeal = doc.createElement("doctor")
            doctorXmlAppeal.setAttribute('first_name', doctor.get_first_name())
            doctorXmlAppeal.setAttribute('last_name', doctor.get_last_name())
            doctorXmlAppeal.setAttribute('father_name', doctor.get_father_name())
            doctorXmlAppeal.setAttribute('category', doctor.get_category())
            doctorXmlAppeal.setAttribute('specialty', doctor.get_specialty())
            appealXml.appendChild(doctorXmlAppeal)
            patient = appeal.get_Patient()
            patientXmlAppeal = doc.createElement("patient")
            patientXmlAppeal.setAttribute('first_name', patient.get_first_name())
            patientXmlAppeal.setAttribute('last_name', patient.get_last_name())
            patientXmlAppeal.setAttribute('father_name', patient.get_father_name())
            patientXmlAppeal.setAttribute('date_of_birth', patient.get_date_of_birth())
            appealXml.appendChild(patientXmlAppeal)
            root.appendChild(appealXml)
        xml_str = doc.toprettyxml(indent="  ")
        with open("newData.xml", "w") as f:
            f.write(xml_str)
