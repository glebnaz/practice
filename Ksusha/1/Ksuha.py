class general():
    def __init__(self, code = 0):
        self.setCode(code)
    def setCode(self, value):
        self.code = value
    def getCode(self):
        return self.code

class types(general):
    def __init__(self, code = 0, name = '', yp = '', rate = '', term = ''):
        general.__init__(self, code)
        self.setName(name)
        self.setYp(yp)
        self.setRate(rate)
        self.setTerm(term)

    def setName(self, value):self.__name = value
    def setYp(self, value):self.__yp = value
    def setRate(self, value):self.__rate = value
    def setTerm(self, value):self.__term = value
    def getName(self):return self.__name
    def getYp(self):return self.__yp
    def getRate(self):return self.__rate
    def getTerm(self):return self.__term

    def __str__(self):
        return str(self.code) + ' ' + self.__name + ' ' + self.__yp + ' ' + self.__rate + ' ' + self.__term


class clients(general):
    def __init__(self, code = 0, name = '', vs = '', address = '', phone = '', kl = ''):
        general.__init__(self, code)
        self.setCode(code)
        self.setName(name)
        self.setVs(vs)
        self.setAddress(address)
        self.setPhone(phone)
        self.setKl(kl)

    def setName(self,value):self.__name=value
    def setVs(self,value):self.__vs=value
    def setAddress(self,value):self.__address=value
    def setPhone(self,value):self.__phone=value
    def setKl(self,value):self.__kl=value
    def getName(self):return self.__name
    def getVs(self):return self.__vs
    def getAddress(self):return self.__address
    def getPhone(self):return self.__phone
    def getKl(self):return self.__kl

    def __str__(self):
        return str(self.code) + ' ' + self.__name + ' ' + self.__vs + ' ' + \
                self.__address + ' ' + self.__phone + ' ' + self.__kl

class loans(general):
    def __init__(self, code = 0, vk = '', customer = '', amount = '', dv = ''):
        general.__init__(self, code)
        self.setCode(code)
        self.setVk(vk)
        self.setCustomer(customer)
        self.setAmount(amount)
        self.setDv(dv)

    def setVk(self,value):self.__vk=value
    def setCustomer(self,value):self.__customer=value
    def setAmount(self,value):self.__amount=value
    def setDv(self,value):self.__dv=value
    def getVk(self):return self.__vk
    def getCustomer(self):return self.__customer
    def getAmount(self):return self.__amount
    def getDv(self):return self.__dv

    def __str__(self):
        return str(self.code) + ' ' + self.__vk + ' ' + self.__customer + ' ' + \
                self.__amount + ' ' + self.__dv

a = types(20, 'Alexey', 'asa', 'afa', 'af')
b = clients(21, 'Gleb', 'afas', 'safa', 'lkfa', 'asf')
c = loans(214, 'sfas', 'oaf', 'alfn', 'afa;m')
print(a)
print(b)
print(c)
