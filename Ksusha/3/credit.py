class credit:
    def __init__(self,typeOfCredit,client,cost,data):
        self.setClient(client)
        self.setTypeOfCredit(typeOfCredit)
        self.setCost(cost)
        self.setData(data)

    def setId(self,value):
        print("Set ID")
        self.__id = value

    def setTypeOfCredit(self,value):
        print("Set typeOfCredit")
        self.__typeOfCredit = value

    def setClient(self,value):
      print("Set client")
      self.__client = value

    def setData(self,value):
      print("Set data")
      self.__data = value

    def setCost(self,value):
        print("Set phone")
        self.__cost = value

    def getTypeOfCredit(self):
        return self.__typeOfCredit

    def getClient (self):
        return self.__client


    def getCost(self):
        return self.__cost

    def getId(self):
        return self.__Id

    def getData(self):
        return self.__data

    def __str__(self):
        return str(self.getClient()) + ", " + str(self.getTypeOfCredit()) + ", " + self.getCost() + ", " \
            + self.getData()+"."
