class generalList:
  def __init__(self): self.__list = []
  def clear(self): self.__list = []
  def findById(self, id): 
    for l in self.__list:
      if l.getId() == id:
        return l
        break
  def getIds(self): return [s.getId() for s in self.__list]
  def appendList(self, val): self.__list.append(val)
  def removeList(self, id):
    for s in self.__list:
      if s.getId() == id: self.__list.remove(s)
  def getName(self, id): self.findById(id).getName()
  def getYear(self, id): self.findById(id).getYear()