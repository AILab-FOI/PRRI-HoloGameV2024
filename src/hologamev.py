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

def TIC():
 Render()
 enemyMovement()
 Projektili()


t=0
x=96
y=24

minY=120 #najniza tocka
minX=225 #najdesnija tocka


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


	#ispis
	cls(13)
	spr(1+t%60//30*2,x,y,14,1,0,0,2,2)
	t=t+1


class enemy:
  x = 200  
  y = 120
  sprite = 1  
  dx = -1  
  dy = 0
  desno = False
  #shotTimer = 0  # timer za pucanje

class Projectile:
  def __init__(self, x, y):  # konstruktor klase
    self.x = x
    self.y = y
    self.dx = 1 
    self.dy = 0
    self.speed = 5  # brzina projektila
    self.desno = True




#lista projektila
projectiles = []


shotTimer = 0  # timer za pucanje
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
  shotTimer += 1  # svaki frame se povecava za 1

  # puca svakih dvije sekunde
  if shotTimer >= 60 * 2:
    shootProjectile()  # poziv funkcije za pucanje
    shotTimer = 0  # resetiranje timera
    
      

def shootProjectile():
  # kreiranje projektila
  projectile = Projectile(enemy.x + 5, enemy.y) 

  projectile.desno = enemy.desno
  # doda projektil u listu
  projectiles.append(projectile)
  
  
def Projektili():
  for projektil in projectiles:
    if projektil.desno == True:
      projektil.x = projektil.x + projektil.speed
    else:
      projektil.x = projektil.x - projektil.speed

    if projektil.x < 0 or projektil.x > 240:
     del projektil




def Render():
    cls(13)

    for projectile in projectiles:
     spr(80, projectile.x, projectile.y, 14, 1, 0, 0, 1, 1)

    if enemy.desno==True:
        spr(5,enemy.x,enemy.y,14,1,1,0,2,2)
    else:
        spr(5,enemy.x,enemy.y,14,1,0,0,2,2)

    spr(1+t%60//30*2,x,y,14,1,1,0,2,2)
    t=t+1



def test( a, b ):
    return a+b
# <TILES>
# 001:eccccccccc888888caaaaaaaca888888cacccccccacc0ccccacc0ccccacc0ccc
# 002:ccccceee8888cceeaaaa0cee888a0ceeccca0ccc0cca0c0c0cca0c0c0cca0c0c
# 003:eccccccccc888888caaaaaaaca888888cacccccccacccccccacc0ccccacc0ccc
# 004:ccccceee8888cceeaaaa0cee888a0ceeccca0cccccca0c0c0cca0c0c0cca0c0c
# 005:eccccccccceeeeeec6666666c6eeeeeec6b00bbbc6bb00b0c6bb20b0c00b2bbb
# 006:ccccceeeeeeeccee66665ceeeee65cee00b65ccc0bb65c0c2bb65c0c2bb65c0c
# 017:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 018:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
# 019:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 020:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
# 021:c00bbbbbc2006666c2666000c6666000c6666666ceeeeeeecc555cccecccccec
# 022:bb0055cc60065cce66265cee66265cee66665ceeeeeeccee555cceeecccceeee
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

