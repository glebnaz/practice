from general import general

class song(general):
  def __init__(self,id=0, name='', year=0, duration=''):
    general.__init__(self, id, name, year)
    self.setDuration(duration)
  def setDuration(self, duration): self.__duration = duration
  def getDuration(self): return self.__duration

