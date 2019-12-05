class general:
  def __init__(self, id=0, name='', year=0):
    self.setId(id)
    self.setName(name)
    self.setYear(year)
  def setId(self, id): self.__id = id
  def setName(self, name): self.__name = name
  def setYear(self, year): self.__year = year
  def getId(self): return self.__id
  def getName(self): return self.__name
  def getYear(self): return self.__year