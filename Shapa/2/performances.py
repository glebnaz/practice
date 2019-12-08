class performances:
    def __init__(self,name='',year='',budget=0.0):
        self.setName(name)
        self.setbudget(budget)
        self.setyear(year)

    def setId(self,value):
        print("Set ID")
        self.__id = value

    def setName(self,value):
        print("Set Name")
        self.__name = value

    def setbudget(self,value):
        print("Set budget")
        self.__budget = value

    def setyear(self,value):
        print("Set year")
        self.__year = value

    def getName(self):
        return self.__name

    def getbudget (self):
        return self.__budget

    def getyear(self):
        return self.__year

    def getId(self):
        return self.__Id

    def __str__(self):
        return self.getName() + ", " + self.getyear() + ", " + str(self.getbudget()) + "."
