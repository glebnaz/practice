from generallist import generalList

class generalListEdit(generalList):
  def getNewId(self):
    m = 0
    for id in self.getIds():
      if (id > m): m = id
    return m + 1
  def setName(self, id, value): return self.findById(id).setName(value)
  def setYear(self, id, value): return self.findById(id).setYear(value)
