class auto:
    def __init__(self,mark='',cost='',caseCost=0.0,typ=''):
        self.setmark(mark)
        self.setcaseCost(caseCost)
        self.settyp(typ)
        self.setcost(cost)

    def setId(self,value):
        self.__id = value

    def setmark(self,value):
        self.__mark = value

    def settyp(self,value):
        self.__typ = value

    def setcaseCost(self,value):
        self.__caseCost = value

    def setcost(self,value):
        self.__cost = value

    def getmark(self):
        return self.__mark

    def getcaseCost (self):
        return self.__caseCost

    def getcost(self):
        return self.__cost

    def getId(self):
        return self.__id

    def gettyp(self):
        return self.__typ

    def __str__(self):
        return self.getmark() + ", " + self.getcost() + ", " + str(self.getcaseCost()) + " "+self.gettyp()+"."
