class client:
    def __init__(self,firstName='',lastName='',fatherName="",adress="",phone=""):
        self.setfirstName(firstName)
        self.setlastName(lastName)
        self.setfatherName(fatherName)
        self.setadress(adress)
        self.setphone(phone)

    def setId(self,value):
        self.__id = value

    def setfirstName(self,value):
        self.__firstName = value

    def setfatherName(self,value):
        self.__fatherName = value

    def setphone(self,value):
        self.__phone = value

    def setadress(self,value):
        self.__adress = value

    def setlastName(self,value):
        self.__lastName = value

    def getfirstName(self):
        return self.__firstName

    def getphone (self):
        return self.__phone

    def getfatherName (self):
        return self.__fatherName

    def getadress(self):
        return self.__adress

    def getlastName(self):
        return self.__lastName

    def getId(self):
        return self.__id

    def __str__(self):
        return self.getfirstName() + ", " + self.getlastName() + ", " + self.getadress() + ", " \
            + self.getfatherName()+","+self.getphone()+"."
