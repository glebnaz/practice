class types:
    def __init__(self,name='',conditional='',rate=0.0,term=""):
        self.setName(name)
        self.setRate(rate)
        self.setTerm(term)
        self.setConditional(conditional)

    def setId(self,value):
        print("Set ID")
        self.__id = value

    def setName(self,value):
        print("Set Name")
        self.__name = value

    def setRate(self,value):
        print("Set Rate")
        self.__rate = value

    def setTerm(self,value):
        print("Set Term")
        self.__term = value

    def setConditional(self,value):
        print("Set Conditional")
        self.__conditional = value

    def getName(self):
        return self.__name

    def getTerm (self):
        return self.__term

    def getRate (self):
        return self.__rate

    def getConditional(self):
        return self.__conditional

    def getId(self):
        return self.__id

    def __str__(self):
        return self.getName() + ", " + self.getConditional() + ", " + str(self.getRate()) + ", " \
            + self.getTerm()+"."
