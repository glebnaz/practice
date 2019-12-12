class case:
    def __init__(self,client,autos,dateout,datereturn):
        self.setautos(autos)
        self.setclient(client)
        self.setdateout(dateout)
        self.setdatereturn(datereturn)

    def setId(self,value):
        print("Set ID")
        self.__id = value

    def setclient(self,value):
        print("Set client")
        self.__client = value

    def setautos(self,value):
      print("Set autos")
      self.__autos = value

    def setdatereturn(self,value):
      print("Set datereturn")
      self.__datereturn = value

    def setdateout(self,value):
        print("Set phone")
        self.__dateout = value

    def getclient(self):
        return self.__client

    def getautos (self):
        return self.__autos


    def getdateout(self):
        return self.__dateout

    def getId(self):
        return self.__Id

    def getdatereturn(self):
        return self.__datereturn

    def __str__(self):
        return str(self.getautos()) + ", " + str(self.getclient()) + ", " + self.getdateout() + ", " \
            + self.getdatereturn()+"."
