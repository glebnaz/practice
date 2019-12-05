import os
import sqlite3 as db

emptydb = """
PRAGMA foreign_keys = ON;

create table singer
(id integer primary key,
name text,
year integer,
surname text,
nickname text);

create table song
(id integer primary key,
name text,
year integer,
duration text);

create table groupp
(id integer primary key,
name text,
year integer,
producer text);

create table groupp_singer
(id integer primary key autoincrement,
groupp integer references groupp(id) on update cascade on delete cascade,
singer integer references singer(id) on update cascade on delete cascade,
unique(groupp,singer));

create table groupp_song
(id integer primary key autoincrement,
groupp integer references groupp(id) on update cascade on delete cascade,
song integer references song(id) on update cascade on delete cascade,
unique(groupp,song));
"""

class datasql:
  def read(self,inp,mus):
    conn = db.connect(inp)
    curs = conn.cursor()
    curs.execute('select * from singer')
    data=curs.fetchall()
    for r in data:mus.newSinger(r[0],r[1],r[2],r[3],r[4])
    curs.execute('select * from song')
    data=curs.fetchall()
    for r in data:mus.newSong(r[0],r[1],r[2],r[3])
    curs.execute('select * from groupp')
    data=curs.fetchall()
    for r in data:mus.newGroup(r[0],r[1],r[2],r[3])
    curs.execute('select groupp,singer from groupp_singer')
    data=curs.fetchall()
    for r in data:mus.appendGroupSinger(r[0],mus.findSingerById(r[1]))
    curs.execute('select groupp,song from groupp_song')
    data=curs.fetchall()
    for r in data:mus.appendGroupSong(r[0],mus.findSongById(r[1]))
    conn.close()
  def write(self,out,mus):
    conn = db.connect(out)
    curs = conn.cursor()
    curs.executescript(emptydb)
    
    for c in mus.getSingerIds():
      curs.execute("insert into singer(id,name, year, surname, nickname) values('%s','%s','%s','%s','%s')"%(
        str(c),
        mus.getSingerName(c),
        str(mus.getSingerYear(c)),
        mus.getSingerSurname(c),
        mus.getSingerNickname(c)))
    for c in mus.getSongIds():
      curs.execute("insert into song(id,name,year,duration) values('%s','%s','%s','%s')"%(
      str(c),mus.getSongName(c),str(mus.getSongYear(c)),mus.getSongDuration(c)))
    for c in mus.getGroupIds():
      curs.execute("insert into groupp(id,name,year,producer) values('%s','%s','%s','%s')"%(
      str(c),
      mus.getGroupName(c),
      str(mus.getGroupYear(c)),
      mus.getGroupProducer(c)))
      for ac in mus.getGroupSingerIds(c):
        curs.execute("insert into groupp_singer(groupp,singer) values('%s','%s')"%(str(c),str(ac)))
      for ac in mus.getGroupSongIds(c):
        curs.execute("insert into groupp_song(groupp,song) values('%s','%s')"%(str(c),str(ac)))
    conn.commit()
    conn.close()
