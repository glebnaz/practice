class labor:
    def __init__(self,actor,performances,cost,role):
        self.setperformances(performances)
        self.setactor(actor)
        self.setCost(cost)
        self.setrole(role)

    def setId(self,value):
        print("Set ID")
        self.__id = value

    def setactor(self,value):
        print("Set actor")
        self.__actor = value

    def setperformances(self,value):
      print("Set performances")
      self.__performances = value

    def setrole(self,value):
      print("Set role")
      self.__role = value

    def setCost(self,value):
        print("Set phone")
        self.__cost = value

    def getactor(self):
        return self.__actor

    def getperformances(self):
        return self.__performances


    def getCost(self):
        return self.__cost

    def getId(self):
        return self.__Id

    def getrole(self):
        return self.__role

    def __str__(self):
        return str(self.getperformances()) + ", " + str(self.getactor()) + ", " + self.getCost() + ", " \
            + self.getrole()+"."
