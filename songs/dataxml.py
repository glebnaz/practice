import os,xml.dom.minidom

class dataxml:
  def read(self,inp,mus):
    dom=xml.dom.minidom.parse(inp)
    dom.normalize()
    for node in dom.childNodes[0].childNodes:
      if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='singer'):
        id,name,year,surname,nickname=0,"",0,"",""
        for t in node.attributes.items():
          if t[0]=="id":id=int(t[1])
          if t[0]=="name":name=t[1]
          if t[0]=="year":year=int(t[1])
          if t[0]=="surname":surname=t[1]
          if t[0]=="nickname":nickname=t[1]
        mus.newSinger(id,name,year,surname,nickname)
      if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='song'):
        id,name,year,duration=0,"",0,""
        for t in node.attributes.items():
          if t[0]=="id":id=int(t[1])
          if t[0]=="name":name=t[1]
          if t[0]=="year":year=int(t[1])
          if t[0]=="duration":duration=t[1]
        mus.newSong(id,name,year,duration)
      if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='group'):
        id,name,year,producer=0,"",0,""
        for t in node.attributes.items():
          if t[0]=="id":id=int(t[1])
          if t[0]=="name":name=t[1]
          if t[0]=="year":year=int(t[1])
          if t[0]=="producer":producer=t[1]
        mus.newGroup(id,name,year,producer)
        for n in node.childNodes:
          if (n.nodeType==n.ELEMENT_NODE)and(n.nodeName=='singer'):
            for t in n.attributes.items():
              if t[0]=="id":singer=mus.findSingerById(int(t[1]))
            mus.appendGroupSinger(id,singer)
          if (n.nodeType==n.ELEMENT_NODE)and(n.nodeName=='song'):
            for t in n.attributes.items():
             if t[0]=="id":song=mus.findSongById(int(t[1]))
            mus.appendGroupSong(id,song)
  def write(self,out,mus):
    dom=xml.dom.minidom.Document()
    root=dom.createElement("music")
    dom.appendChild(root)
    for c in mus.getSingerIds():
      sngr=dom.createElement("singer")
      sngr.setAttribute('id',str(c))
      sngr.setAttribute('name',mus.getSingerName(c))
      sngr.setAttribute('year',str(mus.getSingerYear(c)))
      sngr.setAttribute('surname',mus.getSingerSurname(c))
      sngr.setAttribute('nickname',mus.getSingerNickname(c))
      root.appendChild(sngr)
    for c in mus.getSongIds():
      sng=dom.createElement("song")
      sng.setAttribute('id',str(c))
      sng.setAttribute('name',mus.getSongName(c))
      sng.setAttribute('year',str(mus.getSongYear(c)))
      sng.setAttribute('duration',mus.getSongDuration(c))
      root.appendChild(sng)
    for c in mus.getGroupIds():
      grp=dom.createElement("group")
      grp.setAttribute('id',str(c))
      grp.setAttribute('name',mus.getGroupName(c))
      grp.setAttribute('year', str(mus.getGroupYear(c)))
      grp.setAttribute('producer',mus.getGroupProducer(c))
      for ac in mus.getGroupSingerIds(c):
        sngr=dom.createElement("singer")
        sngr.setAttribute('id',str(ac))
        grp.appendChild(sngr)
        root.appendChild(grp)
      for ac in mus.getGroupSongIds(c):
        sng=dom.createElement("song")
        sng.setAttribute('id',str(ac))
        grp.appendChild(sng)
        root.appendChild(grp)
    f = open(out,"wb")
    f.write(dom.toprettyxml(encoding='utf-8'))
