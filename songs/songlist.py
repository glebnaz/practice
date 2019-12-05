from generallist import generalList

class songList(generalList):
  def getDuration(self, id): return self.findById(id).getDuration()
  def getName(self, id): return self.findById(id).getName()
  def getYear(self, id): return self.findById(id).getYear()
  def getListSongs(self):
    s = ''
    for id in self.getIds():
      s += self.getName(id) + ', '
    if s: s = s[:-2]
    return s