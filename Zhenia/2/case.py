from client import client
from auto import auto
class case:
    def __init__(self,client,autos,dateout,datereturn):
        self.setautos(autos)
        self.setclient(client)
        self.setdateout(dateout)
        self.setdatereturn(datereturn)

    def setId(self,value):
        self.__id = value

    def setclient(self,value):
        self.__client = value

    def setautos(self,value):
      self.__autos = value

    def setdatereturn(self,value):
      self.__datereturn = value

    def setdateout(self,value):
        self.__dateout = value

    def getclient(self):
        return self.__client

    def getautos (self):
        return self.__autos


    def getdateout(self):
        return self.__dateout

    def getId(self):
        return self.__id

    def getdatereturn(self):
        return self.__datereturn

    def __str__(self):
        return str(self.getautos()) + ", " + str(self.getclient()) + ", " + self.getdateout() + ", " \
            + self.getdatereturn()+"."
