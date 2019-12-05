from songlist import songList
from generallistedit import generalListEdit
from song import song

class songListEdit(songList, generalListEdit):
  def newRec(self, id=0, name='', year=0, duration=''): self.appendList(song(id, name, year, duration))
  def setDuration(self, id, value): self.findById(id).setDuration(value)
  