from songlistedit import songListEdit
from singerlistedit import singerListEdit
from grouplistedit import groupListEdit

class music:
  def __init__(self):
    self.__songs = songListEdit()
    self.__singers = singerListEdit()
    self.__groups = groupListEdit()
  def removeSinger(self, id):
    self.__singers.removeList(id)
    for c in self.__groups.getIds():
      self.__groups.removeSinger(c, id)
  def removeSong(self,id):
    self.__songs.removeList(id)
    for c in self.__groups.getIds():
      self.__groups.setSong(c, None)
  def clear(self):
    self.__groups.clear()
    self.__singers.clear()
    self.__songs.clear()
  def newSinger(self, id=0, name='', year=0, surname='', nickname=''): self.__singers.newRec(id, name, year, surname, nickname)
  def findSingerById(self, id): return self.__singers.findById(id)
  def getSingerNewId(self): return self.__singers.getNewId()
  def getSingerIds(self):return self.__singers.getIds()
  def getSingerName(self,id):return self.__singers.getName(id)
  def getSingerYear(self,id):return self.__singers.getYear(id)
  def getSingerSurname(self,id):return self.__singers.getSurname(id)
  def getSingerNickname(self,id):return self.__singers.getNickname(id)
  def setSingerName(self,id,value):self.__singers.setName(id,value)
  def setSingerSurname(self,id,value):self.__singers.setSurname(id,value)
  def setSingerNickname(self,id,value):self.__singers.setNickname(id,value)
  def setSingerYear(self,id,value):self.__singers.setYear(id,value)
  
  def newSong(self, id=0, name='', year=0, duration=''):self.__songs.newRec(id,name,year,duration)
  def findSongById(self,id):return self.__songs.findById(id)
  def getSongNewId(self):return self.__songs.getNewId()
  def getSongIds(self):return self.__songs.getIds()
  def getSongName(self,id):return self.__songs.getName(id)
  def getSongYear(self,id):return self.__songs.getYear(id)
  def getSongDuration(self,id):return self.__songs.getDuration(id)
  def setSongName(self,id,value):self.__songs.setName(id,value)
  def setSongYear(self,id,value):self.__songs.setYear(id,value)
  def setSongDuration(self,id,value):self.__songs.setDuration(id, value)
  def appendGroupSong(self,bid,value):self.__groups.appendSong(bid,value)

  def removeGroup(self,id):self.__groups.removeList(id)
  def newGroup(self, id=0, name='', year=0, producer=''):self.__groups.newRec(id, name, year, producer)
  def findGroupByid(self,id):return self.__groups.findByid(id)
  def appendGroupSinger(self,bid,value):self.__groups.appendSinger(bid,value)
  def removeGroupSinger(self,bid,aid): self.__groups.removeSinger(bid,aid)
  def clearGroupSingers(self,bid):self.__groups.clearSingers(bid)
  def setGroupName(self,id,value):self.__groups.setName(id,value)
  def setGroupYear(self,id,value):self.__groups.setYear(id,value)
  def setGroupProducer(self,id,value):self.__groups.setProducer(id,value)
  def getGroupIds(self):return self.__groups.getIds()
  def getGroupNewId(self):return self.__groups.getNewId()
  def getGroupName(self,id):return self.__groups.getName(id)
  def getGroupYear(self,id):return self.__groups.getYear(id)
  def getGroupProducer(self,id):return self.__groups.getProducer(id)
  def getGroupSingerSurname(self,bid,aid):return self.__groups.getSingerSurname(bid,aid)
  def getGroupSingerName(self,bid,aid):return self.__groups.getSingerName(bid,aid)
  def getGroupSingerYear(self,bid,aid):return self.__groups.getSingerYear(bid,aid)
  def getGroupSingerNickname(self,bid,aid):return self.__groups.getSingerNickname(bid,aid)
  def getGroupSingerIds(self,id):return self.__groups.getSingerIds(id)
  def getGroupSongName(self,bid,aid):return self.__groups.getSongName(bid,aid)
  def getGroupSongYear(self,bid,aid):return self.__groups.getSongYear(bid,aid)
  def getGroupSongDuration(self,bid,aid):return self.__groups.getSongDuration(bid,aid)
  def getGroupSongIds(self,id):return self.__groups.getSongIds(id)
  def getGroupDescription(self,id):return self.__groups.getDescription(id)


