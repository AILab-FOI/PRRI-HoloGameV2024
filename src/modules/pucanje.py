


class prvaPuska:
    x=0
    y=0
    
    desno=False
    
    firerate = 0.6
    speed=16
    dmg=4
    
    explosive=False
    spr=363
    
class drugaPuska:
    x=0
    y=0
    
    desno=False
    
    firerate = 0.1
    speed=6
    dmg=1
    
    explosive=False
    spr=362
    
class trecaPuska:
    x=0
    y=0
    
    desno=False
    
    firerate = 0.2
    speed=9
    dmg=2
    
    explosive=True
    spr=378


metci = []




class Metak:
    x=0
    y=0
    
    width=4
    height=4
    
    desno=False
    
    speed=9
    dmg=2
    
    explosive=True
    spr=378
    coll = []
    
    
    def MetakCheck(metak, colls):
            metak.coll=colls
            if metak.x < 0 or metak.x > pogled.ogranicenjeX or Metak.ProvjeriKolizije(metak, 0, 1):
                if metak in metci:
                    metci.remove(metak)
                    del metak
                else:
                    del metak
            
    
    
    def ProvjeriKolizije(self, xdodatak, ydodatak):
        self.x += xdodatak
        self.y += ydodatak
        for obj in self.coll:
            if obj.check_collision(self):
                self.x -= xdodatak
                self.y -= ydodatak
                return True
        self.x -= xdodatak
        self.y -= ydodatak
        return False



class Puska:
    x=0
    y=0
    
    g1 = 360
    g2 = 361
    g3 = 376
    
    svep = [prvaPuska, drugaPuska, trecaPuska]  # sve puske
    tp = 0   # trenutna puska
    p = [0, 1]  # puske koje imamo
    
    
    def pucaj(puska):
        metak = Metak()  
        metak.x = int(Puska.x)
        metak.y = int(Puska.y)
        metak.desno = player.desno
  
        metak.dmg = Puska.svep[Puska.p[Puska.tp]].dmg
        metak.speed = Puska.svep[Puska.p[Puska.tp]].speed
        metak.explosive = Puska.svep[Puska.p[Puska.tp]].explosive
        metak.spr = Puska.svep[Puska.p[Puska.tp]].spr

        metci.append(metak)
        player.shootTimer=Puska.svep[Puska.p[Puska.tp]].firerate*60
    
    
    def PromijeniPusku():
        if Puska.p[0] == Puska.p[Puska.tp]:
            Puska.tp = 1
        else:
            Puska.tp = 0
    
    
    def Pucanje():
      if player.shootTimer < 0:
        if key(6):
            Puska.pucaj(prvaPuska)
        if key(7):
            Puska.pucaj(drugaPuska)
        if key(8):
            Puska.pucaj(trecaPuska)
        if keyp(19):
            Puska.PromijeniPusku()
      
      eksdes = 12
      fliph = 0
      sprN = 360
      
      # gdje i kako ce se puska renderati
      if player.desno:
        Puska.x = int(player.x) + eksdes
        Puska.y = int(player.y)
      else:
        Puska.x = int(player.x) - int(eksdes / 2)
        Puska.y = int(player.y) 
        fliph = 1
    
    # koji sprite uzimamo
      if Puska.p[Puska.tp] == 1:
          sprN = 361
      elif Puska.p[Puska.tp] == 2:
          sprN = 376
    
      spr(sprN, Puska.x - int(pogled.x), Puska.y - int(pogled.y), 14,1,fliph,0,1,1)
    
      player.shootTimer = player.shootTimer - 1
        
      for metak in metci:
            spr(metak.spr,metak.x - int(pogled.x),metak.y - int(pogled.y),14,1,0,0,1,1)
            
            if metak.desno == True:   
                metak.x = metak.x + metak.speed
            else:
                metak.x = metak.x - metak.speed

            
class PromjenaPuska:
    puskaBr = 0
    x = 0
    y = 0






