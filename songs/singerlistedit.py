from singerlist import singerList
from generallistedit import generalListEdit
from singer import singer

class singerListEdit(singerList, generalListEdit):
  def newRec(self, id=0, name='', year=0, surname='', nickname=''): self.appendList(singer(id, name, year, surname, nickname))
  def setSurname(self, id, value): self.findById(id).setSurname(value)
  def setNickname(self, id, value): self.findById(id).setNickname(value)