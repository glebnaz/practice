import xml.dom.minidom
from Doctor import Doctor
from Patient import Patient
from Appeal import Appeal
class dataxml:
    def __init__(self, filename):
        self.filename = filename
        print(self.filename)
        self.doctorsList = dict()
        self.patientsList = dict()
        self.appealList = dict()



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
        doctors = doc.createElement("doctors")
        for doctorId in self.doctorsList:
            doctor = self.doctorsList[doctorId]
            doctorXml = doc.createElement("doctor")
            doctorXml.setAttribute('first_name', doctor.get_first_name())
            doctorXml.setAttribute('last_name', doctor.get_last_name())
            doctorXml.setAttribute('father_name', doctor.get_father_name())
            doctorXml.setAttribute('category', doctor.get_category())
            doctorXml.setAttribute('specialty', doctor.get_specialty())
            doctors.appendChild(doctorXml)
        root.appendChild(doctors)
        patients = doc.createElement("patients")
        for patientId in self.patientsList:
            patient = self.patientsList[patientId]
            patientXml = doc.createElement("patient")
            patientXml.setAttribute('first_name', patient.get_first_name())
            patientXml.setAttribute('last_name', patient.get_last_name())
            patientXml.setAttribute('father_name', patient.get_father_name())
            patientXml.setAttribute('date_of_birth', patient.get_date_of_birth())
            patients.appendChild(patientXml)
        root.appendChild(patients)
        appeals = doc.createElement("appeals")
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
            appeals.appendChild(appealXml)
        root.appendChild(appeals)
        xml_str = doc.toprettyxml(indent="  ")
        with open("newData.xml", "w") as f:
            f.write(xml_str)
