# title:   HoloGameV
# author:  AILab-FOI
# desc:    short description
# site:    https://ai.foi.hr
# license: GPLv3
# version: 0.1
# script:  python

t=0

def TIC():
 Final()
 Pucanje()
 PlayerKontroler()




def Final():
	cls(13)
    print("A i D za kretanje, SPACE za skakanje", 0, 0)
    print("W za jetpack, F i G za pucanje", 0, 8)
 
	t=t+1

#class collidable:
#    def __init__(self, x, y, width, height):
#        self.x = x
#        self.y = y
#        self.width = width
#        self.height = height
#
#    def check_collision(self, other):
#        if (self.x < other.x + other.width and
#            self.x + self.width > other.x and
#            self.y < other.y + other.height and
#            self.y + self.height > other.y):
#            return True
#        return False
#
#class platforma(collidable):
#    def __init__(self, x, y, width, height):
#        super().__init__(x, y, width, height)




class player: 
    x=96
    y=24
    hsp=0
    vsp=0
    desno=False
    shootTimer=0
    jetpackGorivo=0
    skok=0 
    


minY=120 #najniza tocka
minX=225 #najdesnija tocka

#Osnovne Varijable
akceleracija=0.5
maxBrzina=3
gravitacija=0.3

#Varijable skakanja
skokJacina=5.2

#jetpack
jetpackTrajanje=50
jetpackJacina=5


def pomakni(a, b, vrijednost):
    if vrijednost == 0:
        return a
    elif a < b:
        return min(a + vrijednost, b)
    else:
        return max(a - vrijednost, b)



def PlayerKontroler():
     #skakanje
    if key(48) and player.vsp==0:
	    if player.y>=minY:
            player.vsp=-skokJacina # ZAMIJENITI SA COLLISION PROVJEROM


    #kretanje lijevo desno
    if key(1): 
        #player.x=player.x-brzina
        player.hsp=pomakni(player.hsp,-maxBrzina,akceleracija)
        player.desno=False
    elif key(4):
        #player.x=player.x+brzina
        player.hsp=pomakni(player.hsp,maxBrzina,akceleracija)
        player.desno=True
    else:
        player.hsp=pomakni(player.hsp,0,akceleracija)

    if key(23):
        JetpackJoyride()
        

    #gravitacija
    if player.y+player.vsp>minY:
        player.vsp=0
        player.y=minY
    else:
        player.vsp=player.vsp+gravitacija

	#blokiranje lijevo i desno
	if player.x>minX: # ZAMIJENITI SA COLLISION PROVJEROM
		player.x=minX
        player.hsp=0
		
    if player.x<0: # ZAMIJENITI SA COLLISION PROVJEROM
        player.x=0
        player.hsp=0

    player.x=player.x+player.hsp
    player.y=player.y+player.vsp
        
    
    #jetpack
    
    if player.y == minY:
        player.jetpackGorivo=jetpackTrajanje
    
        
    #renderanje spritea
    if player.desno==True:
        spr(1+t%60//30*2,int(player.x),int(player.y),14,1,1,0,2,2)
    else:
        spr(1+t%60//30*2,int(player.x),int(player.y),14,1,0,0,2,2)
        
        
def JetpackJoyride():
    if player.jetpackGorivo > 0:
        player.y = player.y - jetpackJacina
        player.jetpackGorivo = player.jetpackGorivo - 1
        player.skok = 0
     
        






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


metci = []



   

def Pucanje():
    
    player.shootTimer = player.shootTimer - 1
    
    if player.shootTimer < 0:
        if key(6):
            pucaj(prvaPuska)
        if key(7):
            pucaj(drugaPuska)
        
    for metak in metci:
            spr(1,metak.x,metak.y,14,1,0,1,1,1)
            
            if metak.desno == True:   
                metak.x = metak.x + metak.speed
            else:
                metak.x = metak.x - metak.speed
            
            if metak.x < 0 or metak.x > minX:
                del metak

def pucaj(puska):
  metak = puska()  
  metak.x = player.x
  metak.y = player.y
  metak.desno = player.desno

  metci.append(metak)
  player.shootTimer=puska.firerate*60
  




def test( a, b ):
    return a+b
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

