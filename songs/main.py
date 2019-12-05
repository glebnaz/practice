"""
from music import music
from dataxml import dataxml as data

mus1 = music()
dat1 = data()
dat1.read('old.xml', mus1)
dat1.write('new.xml', mus1)
for id in mus1.getGroupIds():
 print(mus1.getGroupDescription(id))
"""

from music import music
from dataxml import dataxml as datax
from datasql import datasql as data

mus1 = music()
dat1 = datax()
dat1.read("old.xml",mus1)
dat2 = data()
dat2.write("new5.sqlite",mus1)
dat2.read("new5.sqlite", mus1)
for id in mus1.getGroupIds():
 print(mus1.getGroupDescription(id))
