#lista projektila
projectiles = []

class enemy:
  x = 200  
  y = 120
  sprite = 1  
  dx = -1  
  dy = 0
  desno = False
  shotTimer = 0  # timer za pucanje

  def movement(self):
    self.x = self.x + self.dx
    self.y = self.y + self.dy
    if self.x <= 0:
      self.dx = 1  # mijenja stranu kad takne lijevu stranu
      self.desno = True
    elif self.x >= pogled.ogranicenjeX:
      self.dx = -1  # mijenja stranu kad takne desnu stranu
      self.desno = False

    self.shotTimer += 1  # svaki frame se povecava za 1

    # puca svakih dvije sekunde
    if self.shotTimer >= 60 * 2:
      self.shootProjectile(self)  # poziv funkcije za pucanje
      self.shotTimer = 0  # resetiranje timera

  def shootProjectile(self):
    projectile = Projectile(self.x + 5, self.y) 

    projectile.desno = self.desno
    # doda projektil u listu
    projectiles.append(projectile)

class Projectile:
  def __init__(self, x, y):  # konstruktor klase
    self.x = x
    self.y = y
    self.dx = 1 
    self.dy = 0
    self.speed = 5  # brzina projektila
    self.desno = True
  
  
def Projektili():
  for projektil in projectiles:
    if projektil.desno == True:
      projektil.x = projektil.x + projektil.speed
    else:
      projektil.x = projektil.x - projektil.speed

    if projektil.x < 0 or projektil.x > 240:
     del projektil




def RenderBullets():
    for projectile in projectiles:
     spr(80, projectile.x - int(pogled.x), projectile.y - int(pogled.y), 14, 1, 0, 0, 1, 1)

    if enemy.desno==True:
        spr(290,enemy.x - int(pogled.x),enemy.y - int(pogled.y),6,1,0,0,2,2)
    else:
        spr(290,enemy.x - int(pogled.x),enemy.y - int(pogled.y),6,1,1,0,2,2)