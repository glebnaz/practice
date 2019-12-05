from generallist import generalList

class singerList(generalList):
  def getYear(self, id): return self.findById(id).getYear()
  def getName(self, id): return self.findById(id).getName()
  def getSurname(self, id): return self.findById(id).getSurname()
  def getNickname(self, id): return self.findById(id).getNickname()
  def getListSingers(self):
    s = ''
    for id in self.getIds():
      s += self.getName(id) + ' ' + self.getSurname(id) + ', '
    if s: s = s[:-2]
    return s