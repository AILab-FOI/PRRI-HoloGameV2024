


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


def Pucanje():
    
    player.shootTimer = player.shootTimer - 1
    
    if player.shootTimer < 0:
        if key(6):
            pucaj(prvaPuska)
        if key(7):
            pucaj(drugaPuska)
        if key(8):
            pucaj(trecaPuska)
        
    for metak in metci:
            spr(metak.spr,metak.x - int(pogled.x),metak.y - int(pogled.y),14,1,0,0,1,1)
            
            if metak.desno == True:   
                metak.x = metak.x + metak.speed
            else:
                metak.x = metak.x - metak.speed
            
                
                
            
            
            

def pucaj(puska):
  metak = Metak()  
  metak.x = int(player.x)
  metak.y = int(player.y)
  metak.desno = player.desno
  
  metak.dmg = puska.dmg
  metak.speed = puska.speed
  metak.explosive = puska.explosive
  metak.spr = puska.spr

  metci.append(metak)
  player.shootTimer=puska.firerate*60
  



