from general import general
from singerlist import singerList
from songlist import songList

class group(general):
  def __init__(self, id=0, name='', year=0, producer=''):
    general.__init__(self, id, name, year)
    self.setProducer(producer)
    self.__singers = singerList()
    self.__songs = songList()
  def setProducer(self, producer): self.__producer = producer
  def getProducer(self): return self.__producer
  def appendSinger(self, val): self.__singers.appendList(val)
  def removeSinger(self, id): self.__singers.removeList(id)
  def clearSingers(self): self.__singers.clear()
  def getSingerIds(self): return self.__singers.getIds()
  def getSingerYear(self, id): return self.__singers.findById(id).getYear()
  def getSingerName(self, id): return self.__singers.findById(id).getName()
  def getSingerSurname(self, id): return self.__singers.findById(id).getSurname()
  def getSingerNickname(self, id): return self.__singers.findById(id).getNickname()
  def getSingersList(self): return self.__singers.getListSingers()
  def appendSong(self, val): self.__songs.appendList(val)
  def removeSong(self, id): self.__songs.removeList(id)
  def clearSongs(self): self.__songs.clear()
  def getSongIds(self): return self.__songs.getIds()
  def getSongYear(self, id): return self.__singers.findById(id).getYear()
  def getSongName(self, id): return self.__songs.findById(id).getName()
  def getSongDuration(self, id): return self.__songs.findById(id).getDuration()
  def getSongsList(self): return self.__songs.getListSongs()
  def getDescription(self): 
    return self.getName() + '\n' + 'Исполнители: ' + self.__singers.getListSingers() + '\n' + 'Песни: ' + self.__songs.getListSongs() + '\n' + 'Продюсер: ' + self.getProducer() + '\n' + 'Год основания: ' + str(self.getYear())
