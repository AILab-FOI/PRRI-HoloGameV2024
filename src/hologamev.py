# title:   HoloGameV
# author:  AILab-FOI
# desc:    short description
# site:    https://ai.foi.hr
# license: GPLv3
# version: 0.1
# script:  python

t=0


class player: 
    x=96
    y=24
    desno=False
    shootTimer=0
    jet
    
    
    
class prvaPuska:
    x=0
    y=0
    
    desno=False
    
    firerate = 1
    speed=16
    dmg=4
    
class drugaPuska:
    x=0
    y=0
    
    desno=False
    
    firerate = 0.1
    speed=6
    dmg=1


metci = []


initDone = False






minY=120 #najniza tocka
minX=225 #najdesnija tocka

#Osnovne Varijable
brzina=3
gravitacija=2

#jetpack
jetpackTrajanje=3
jetpackJacina=2

#granata
granataVelicinaEksplozije=3

#Varijable skakanja
skokVar=0 
skokTrajanje=20
skokJacina=2






def TIC():
 Init()
 Final()
 Pucanje()
 PlayerKontroler()






def PlayerKontroler():
    global skokVar, skokTrajanje, skokJacina, minY, minX, brzina, gravitacija


     #skakanje
    if btn(0):
	    if player.y==minY:
		    skokVar=skokTrajanje 
                
    if key(48):
        if player.y==minY:
            skokVar=skokTrajanje 
            
    if skokVar>0:
        player.y=player.y-skokJacina
        skokVar=skokVar-1 

    #kretanje lijevo desno
    if btn(2): 
        player.x=player.x-brzina
        player.desno=False
    if btn(3):
        player.x=player.x+brzina
        player.desno=True

    #gravitacija
	if player.y<minY:
		if skokVar<1:
		    player.y=player.y+gravitacija
	else: 
		player.y=minY

	#blokiranje lijevo i desno
	if player.x>minX:
		player.x=minX
		
    if player.x<0:
        player.x=0
        
    
    #jetpack
        
    
        
    #renderanje spritea
    if player.desno==True:
        spr(1+t%60//30*2,player.x,player.y,14,1,1,0,2,2)
    else:
        spr(1+t%60//30*2,player.x,player.y,14,1,0,0,2,2)
        
        
        
        
        

def Pucanje():
    
    player.shootTimer = player.shootTimer - 1
    
    if player.shootTimer < 0:
        if key(6):
            pucajPrvi()
        if key(7):
            pucajDrugi()
        
    for metak in metci:
            spr(1,metak.x,metak.y,14,1,0,1,1,1)
            
            if metak.desno == True:   
                metak.x = metak.x + metak.speed
            else:
                metak.x = metak.x - metak.speed
            
            if metak.x < 0 or metak.x > minX:
                del metak




def pucajPrvi(metak):
  metak = prvaPuska()  
  metak.x = player.x
  metak.y = player.y
  metak.desno = player.desno

  metci.append(metak)
  player.shootTimer=prvaPuska.firerate*60
  
def pucajDrugi():
  metak = drugaPuska() 
  metak.x = player.x
  metak.y = player.y
  metak.desno = player.desno

  metci.append(metak)
  player.shootTimer=drugaPuska.firerate*60





def Init():
    if initDone == False:
        initDone = True
    





def Final():
	cls(13)
    print("F i G za pucanje")
 
	t=t+1


 
 


# <TILES>
# 001:eccccccccc888888caaaaaaaca888888cacccccccacc0ccccacc0ccccacc0ccc
# 002:ccccceee8888cceeaaaa0cee888a0ceeccca0ccc0cca0c0c0cca0c0c0cca0c0c
# 003:eccccccccc888888caaaaaaaca888888cacccccccacccccccacc0ccccacc0ccc
# 004:ccccceee8888cceeaaaa0cee888a0ceeccca0cccccca0c0c0cca0c0c0cca0c0c
# 017:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 018:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
# 019:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 020:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
# </TILES>

# <WAVES>
# 000:00000000ffffffff00000000ffffffff
# 001:0123456789abcdeffedcba9876543210
# 002:0123456789abcdef0123456789abcdef
# </WAVES>

# <SFX>
# 000:000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000304000000000
# </SFX>

# <TRACKS>
# 000:100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# </TRACKS>

# <PALETTE>
# 000:1a1c2c5d275db13e53ef7d57ffcd75a7f07038b76425717929366f3b5dc941a6f673eff7f4f4f494b0c2566c86333c57
# </PALETTE>

