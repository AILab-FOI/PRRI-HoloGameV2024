# title:   HoloGameV
# author:  AILab-FOI
# desc:    short description
# site:    https://ai.foi.hr
# license: GPLv3
# version: 0.1
# script:  python

t=0
x=96
y=24

class enemy:
  x = 200  # Initial position (adjust as needed)
  y = 120
  sprite = 1 # Replace with the enemy's sprite ID
  dx = -1   # Enemy moves left initially
  dy = 0
  desno = False

class projektil:
 def __init__(self, x, y):  # konstruktor
    self.x = x
    self.y = y
    self.dx = 1 
    self.dy = 0
    self.speed = 5
    



def TIC():
 Final()
 PlayerKontroler()
 enemyMovement()
 pucanjeProjektila()
 


t=0
x=96
y=24

minY=120 #najniza tocka
minX=225 #najdesnija tocka

shotTimer = 0
def enemyMovement():
 enemy.x = enemy.x + enemy.dx
 enemy.y = enemy.y + enemy.dy
 if enemy.x <= 0:
    enemy.dx = 1  # mijenja stranu kad takne lijevu stranu
    enemy.desno = True
 elif enemy.x >= minX:
    enemy.dx = -1  # mijenja stranu kad takne desnu stranu
    enemy.desno = False

 global shotTimer
 shotTimer += 1 # timer se povecava se svaki frame

 # puca svakih 5 sekundu
 if shotTimer >= 60 * 5:
    pucanjeProjektila()  # pozivanje funkcije
    shotTimer = 0  # nakon poziva resetira se timer



#Osnovne Varijable
brzina=3
gravitacija=2


#Varijable skakanja
skokVar=0 
skokTrajanje=20
skokJacina=2

def PlayerKontroler():
    global t, x, y, minY, minX, brzina, gravitacija, skokVar, skokTrajanje, skokJacina

     #skakanje
    if btn(0):
	    if y==minY:
		    skokVar=skokTrajanje 
                
    if key(48):
        if y==minY:
            skokVar=skokTrajanje 
    if skokVar>0:
        y=y-skokJacina
        skokVar=skokVar-1 

    #kretanje lijevo desno
    if btn(2): 
        x=x-brzina
    if btn(3):
        x=x+brzina

    #gravitacija
	if y<minY:
		if skokVar<1:
		    y=y+gravitacija
	else: 
		y=minY


	#blokiranje lijevo i desno
	if x>minX:
		x=minX
		
    if x<0:
		x=0
          

def pucanjeProjektila():
  # krira objekt
  projectile = projektil(enemy.x + 5, enemy.y)  # Adjust offset for visual clarity

  # dodavanje projektila u listu
  projectiles.append(projectile)

  # lista za spremanje projektila
projectiles = []
 



	#ispis
def Final():
    cls(13)
    
    #projektil
    for projectile in projectiles:
        spr(80,projectile.x,projectile.y,1,1,0,0,1,1)


    #enemy    
    if enemy.desno==True:
        spr(1+t%60//30*2,enemy.x,enemy.y,14,1,1,0,2,2)
    else:
        spr(1+t%60//30*2,enemy.x,enemy.y,14,1,0,0,2,2)

    #igrac    
    spr(1+t%60//30*2,x,y,14,1,1,0,2,2) 
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
# 080:ddd22ddddd2222ddd22dd22d22d22d2222d22d22d22dd22ddd2222ddddd22ddd
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

