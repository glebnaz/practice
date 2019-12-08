class client:
    def __init__(self,name='',typeOfProperty='',adress="",phone="",person=""):
        self.setName(name)
        self.setTypeOfProperty(typeOfProperty)
        self.setAdress(adress)
        self.setPhone(phone)
        self.setPerson(person)

    def setId(self,value):
        print("Set ID")
        self.__id = value

    def setName(self,value):
          print("Set Name")
          self.__name = value

    def setAdress(self,value):
        print("Set adress")
        self.__adress = value

    def setPerson(self,value):
        print("Set person")
        self.__person = value

    def setPhone(self,value):
        print("Set phone")
        self.__phone = value

    def setTypeOfProperty(self,value):
        print("Set phone")
        self.__typeOfProperty = value

    def getName(self):
        return self.__name

    def getPerson (self):
        return self.__person

    def getAdress (self):
        return self.__adress

    def getPhone(self):
        return self.__phone

    def getTypeOfProperty(self):
        return self.__typeOfProperty

    def getId(self):
        return self.__Id

    def __str__(self):
        return self.getName() + ", " + self.getTypeOfProperty() + ", " + self.getPhone() + ", " \
            + self.getAdress()+","+self.getPerson()+"."
