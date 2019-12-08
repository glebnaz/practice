class actor:
    def __init__(self,firstName='',lastName='',fatherName="",rank="",experience=""):
        self.setfirstName(firstName)
        self.setlastName(lastName)
        self.setfatherName(fatherName)
        self.setrank(rank)
        self.setexperience(experience)

    def setId(self,value):
        print("Set ID")
        self.__id = value

    def setfirstName(self,value):
          print("Set firstName")
          self.__firstName = value

    def setfatherName(self,value):
        print("Set fatherName")
        self.__fatherName = value

    def setexperience(self,value):
        print("Set experience")
        self.__experience = value

    def setrank(self,value):
        print("Set rank")
        self.__rank = value

    def setlastName(self,value):
        print("Set rank")
        self.__lastName = value

    def getfirstName(self):
        return self.__firstName

    def getexperience (self):
        return self.__experience

    def getfatherName (self):
        return self.__fatherName

    def getrank(self):
        return self.__rank

    def getlastName(self):
        return self.__lastName

    def getId(self):
        return self.__Id

    def __str__(self):
        return self.getfirstName() + ", " + self.getlastName() + ", " + self.getrank() + ", " \
            + self.getfatherName()+","+self.getexperience()+"."
