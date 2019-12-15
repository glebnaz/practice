class client:
    def __init__(self,firstName='',lastName='',fatherName="",adress="",phone=""):
        self.setfirstName(firstName)
        self.setlastName(lastName)
        self.setfatherName(fatherName)
        self.setadress(adress)
        self.setphone(phone)

    def setId(self,value):
        print("Set ID")
        self.__id = value

    def setfirstName(self,value):
          print("Set firstName")
          self.__firstName = value

    def setfatherName(self,value):
        print("Set fatherName")
        self.__fatherName = value

    def setphone(self,value):
        print("Set phone")
        self.__phone = value

    def setadress(self,value):
        print("Set adress")
        self.__adress = value

    def setlastName(self,value):
        print("Set last_name")
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
        return self.__Id

    def __str__(self):
        return self.getfirstName() + ", " + self.getlastName() + ", " + self.getadress() + ", " \
            + self.getfatherName()+","+self.getphone()+"."
