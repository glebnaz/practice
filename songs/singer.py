from general import general

class singer(general):
  def __init__(self, id=0, name='', year=0, surname='', nickname=''):
    general.__init__(self, id, name, year)
    self.setSurname(surname)
    self.setNickname(nickname)
  def setSurname(self, surname): self.__surname = surname
  def setNickname(self, nickname): self.__nickname = nickname
  def getSurname(self): return self.__surname
  def getNickname(self): return self.__nickname
