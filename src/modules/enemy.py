

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


