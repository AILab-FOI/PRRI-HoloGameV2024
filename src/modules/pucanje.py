


class prvaPuska:
    x=0
    y=0
    
    desno=False
    
    firerate = 0.6
    speed=16
    dmg=4
    
class drugaPuska:
    x=0
    y=0
    
    desno=False
    
    firerate = 0.1
    speed=6
    dmg=1
    
class trecaPuska:
    x=0
    y=0
    
    desno=False
    
    firerate = 0.2
    speed=9
    dmg=2


metci = []



   

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
            spr(104,metak.x - int(pogled.x),metak.y - int(pogled.y),14,1,0,1,1,1)
            
            if metak.desno == True:   
                metak.x = metak.x + metak.speed
            else:
                metak.x = metak.x - metak.speed
            
            if metak.x < 0 or metak.x > pogled.ogranicenjeX:
                del metak

def pucaj(puska):
  metak = puska()  
  metak.x = int(player.x)
  metak.y = int(player.y)
  metak.desno = player.desno

  metci.append(metak)
  player.shootTimer=puska.firerate*60
  



