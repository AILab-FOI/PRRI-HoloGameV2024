#lista projektila
projectiles = []

class Enemy2(Enemy):
  x = 90 
  y = 90
  width = 16
  height = 16
  sprite = 1  
  dx = -1  
  vsp = 0
  gravitacija = 0.3
  skokJacina = 4
  minY = 120
  desno = False
  shotTimer = 0  # timer za pucanje
  shotFreq = 1 # koliko cesto puca
  coll = []
  health = 4

  def __init__(self, x, y):
    tile_size = 8
    self.x = x*tile_size
    self.y = y*tile_size

  def movement(self, coll):
    self.coll = coll
    self.x = self.x + self.dx
    if not self.dead and self.ProvjeriKolizije(6*self.dx, 0):
      if not self.ProvjeriKolizije(3*self.dx, -9):
        if self.ProvjeriKolizije(0, 1):
          self.vsp = -self.skokJacina
        else:
          self.dx = -self.dx
          self.desno = not self.desno
    elif not self.dead and self.ProvjeriKolizije(3*self.dx, 0):
      self.dx = -self.dx
      self.desno = not self.desno
    if not self.dead and self.x <= 0:
      self.dx = 1  # mijenja stranu kad takne lijevu stranu
      self.desno = True
    elif not self.dead and self.x >= pogled.ogranicenjeX:
      self.dx = -1  # mijenja stranu kad takne desnu stranu
      self.desno = False

    self.shotTimer += 1  # svaki frame se povecava za 1

    # gravitacija
    if self.y+self.vsp>=self.minY or self.ProvjeriKolizije(0, self.vsp + 1):
      self.vsp=0
      while self.y<self.minY and not self.ProvjeriKolizije(0, 1):
        self.y+=1
    else:
      self.vsp=self.vsp+self.gravitacija

    if self.vsp<0:
      if self.ProvjeriKolizije(0, self.vsp - 1):
        self.vsp=0

    self.y = self.y + self.vsp

    # puca svakih 1 sekundu
    if not self.dead and self.shotTimer >= 60 * self.shotFreq:
      self.shootProjectile()  # poziv funkcije za pucanje
      self.shotTimer = 0  # resetiranje timera

    #crtanje samog sebe
    if not self.dead and self.desno==True:
      spr(326,int(self.x) - int(pogled.x),int(self.y) - int(pogled.y),6,1,0,0,2,2)
    elif not self.dead:
      spr(326,int(self.x) - int(pogled.x),int(self.y) - int(pogled.y),6,1,1,0,2,2)

  def shootProjectile(self):
    projectile = Projectile(self.x + 5, int(self.y)) 

    projectile.desno = self.desno
    # doda projektil u listu
    projectiles.append(projectile)

    sfx(3, "E-4", 3, 0, 2, 3)

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
  
  def Pogoden(self, damage, removeInt):
    self.health = self.health - damage
    if self.health < 1:
      self.dead = True