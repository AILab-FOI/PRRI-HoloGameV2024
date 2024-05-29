# title:   HoloGameV
# author:  AILab-FOI
# desc:    short description
# site:    https://ai.foi.hr
# license: GPLv3
# version: 0.1
# script:  python


state='menu' #varijabla za game state

level = 0 # koji level je ucitan (od 0 pa na dalje)

def TIC():
 Final()

 global state
 if state=='game':
   IgrajLevel()
 elif state=='menu':
   menu.Menu()

def Final():
	cls(13) 

class collidable:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #self.draw_self()

    def check_collision(self, other):
        if self.x < other.x + other.width and self.x + self.width > other.x and self.y < other.y + other.height and self.y + self.height > other.y:
            return True
        return False

    def check_collision_rectangle(self, xleft, ytop, xright, ybottom):
        if self.x < xright and self.x + self.width > xleft and self.y < ybottom and self.y + self.height > ytop:
            return True
        return False

    def draw_self(self):
        rect(self.x - int(pogled.x), self.y - int(pogled.y), self.width, self.height, 15)


def DefinirajKolizije(listaObjekata, level, level_height):
    collidables = {}
    # ako objekt nije lista prvi dio koda se raunna, inace je drugi (else)
    tile_size = 8
    for objekt in listaObjekata:
      sirinaKolizija = 8
      if not isinstance (objekt, list):
        px = min(max(int(objekt.x/tile_size) - round(sirinaKolizija/2), 0), 239)
        py = min(max(int(objekt.y/tile_size) - round(sirinaKolizija/2), 0), 135)

        for xx in range(sirinaKolizija):
            for yy in range(sirinaKolizija):
                tileHere = mget(xx + px, yy + py + level*level_height)
                if tileHere != 0 and tileHere not in level_finish_tile_indexes and tileHere not in background_tile_indexes:
                    pos_key = ("x", xx + px, "y", yy + py)
                    if pos_key not in collidables:
                        collidables[pos_key] = collidable((xx + px)*tile_size, (yy + py)*tile_size, tile_size, tile_size)
      else:
          for obj in objekt:
              px = min(max(int(obj.x/tile_size) - round(sirinaKolizija/2), 0), 239)
              py = min(max(int(obj.y/tile_size) - round(sirinaKolizija/2), 0), 135)

              for xx in range(sirinaKolizija):
               for yy in range(sirinaKolizija):
                tileHere = mget(xx + px, yy + py + level*level_height)
                if tileHere != 0 and tileHere not in level_finish_tile_indexes and tileHere not in background_tile_indexes:
                    pos_key = ("x", xx + px, "y", yy + py)
                    if pos_key not in collidables:
                        collidables[pos_key] = collidable((xx + px)*tile_size, (yy + py)*tile_size, tile_size, tile_size)

    return list(collidables.values())




def pomakni(a, b, vrijednost):
    if vrijednost == 0:
        return a
    elif a < b:
        return min(a + vrijednost, b)
    else:
        return max(a - vrijednost, b)

class player: 
    x=96
    y=24
    width=14
    height=14
    hsp=0
    vsp=0
    desno=False
    is_walking = False
    frame = 256
    shootTimer=0
    jetpackGorivo=0
    skok=0
    coll=[]
    spriteTimer = 0

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
    
    minY=120 #najniza tocka
    minX=10000 #najdesnija tocka

    #Osnovne Varijable
    akceleracija=0.5
    maxBrzina=3
    gravitacija=0.3


    #Varijable skakanja
    skokJacina=5.2

    #jetpack
    jetpackTrajanje=50
    jetpackJacina=2
    
    #Koyote time
    coyoteTime=7
    ctVar=0
    jumped=False

    #hp
    health = 3
    hitTimer = 10
    hitVar = 0



    def PlayerKontroler(self, coll):
        self.coll=coll
        #skakanje
        if key(48) and self.vsp == 0: #<- ovo je manje bugged ali bez coyote time  #and not self.jumped:
            if self.ProvjeriKolizije(self, 0, 1) or self.y>=self.minY or self.ctVar < self.coyoteTime:
                self.vsp = -self.skokJacina
                self.jumped = True

        #coyote time
        if self.ProvjeriKolizije(self, 0, 1):
            self.ctVar = 0
            self.jumped = False
        else:
            self.ctVar += 1
        

        #kretanje lijevo desno
        if key(1): 
            self.hsp=pomakni(self.hsp,-self.maxBrzina,self.akceleracija)
            self.desno=False
            self.is_walking = True
        elif key(4):
            self.hsp=pomakni(self.hsp,self.maxBrzina,self.akceleracija)
            self.is_walking = True
            self.desno=True
        else:
            self.hsp=pomakni(self.hsp,0,self.akceleracija)
            self.is_walking = False

        if key(23):
            self.JetpackJoyride(self)
            

        #gravitacija i kolizije
        if self.y+self.vsp>=self.minY or self.ProvjeriKolizije(self, 0, self.vsp + 1):
            while self.y<self.minY and not self.ProvjeriKolizije(self, 0, 1):
                self.y+=1
            self.vsp=0
        else:
            self.vsp=self.vsp+self.gravitacija

        if self.vsp<0:
            if self.ProvjeriKolizije(self, 0, self.vsp - 1):
                self.vsp=0

        

        #blokiranje lijevo i desno
        if self.x>(pogled.ogranicenjeX - self.width) or self.ProvjeriKolizije(self, 1+self.hsp, 0):
            self.hsp=0
            while self.x > (pogled.ogranicenjeX - self.width):
                self.x-=1
            
        if self.x<0 or self.ProvjeriKolizije(self, -1+self.hsp, 0):
            self.hsp=0
            while self.x < 0:
                self.x+=1

        self.x=self.x+self.hsp
        self.y=self.y+self.vsp
            
        
        #jetpack
        
        if self.ProvjeriKolizije(self, 0, 1) or self.y>=self.minY: # ZAMIJENITI SA DOK STOJI NA NEKOM OBJEKTU
            self.jetpackGorivo=self.jetpackTrajanje

        if self.is_walking == True:
            self.spriteTimer += 0.1

        #renderanje spritea
        if self.desno==True and self.is_walking==True:
            spr(258 + 2*(round(self.spriteTimer)%2==0),int(self.x) - int(pogled.x),int(self.y) - int(pogled.y),6,1,0,0,2,2)
        elif self.desno==False and self.is_walking==True:
            spr(258 + 2*(round(self.spriteTimer)%2==0),int(self.x) - int(pogled.x),int(self.y) - int(pogled.y),6,1,1,0,2,2)
        else:
            spr(self.frame,int(self.x) - int(pogled.x),int(self.y) - int(pogled.y),6,1,int(self.desno==False),0,2,2)


        if self.hitTimer > self.hitVar:
            self.hitVar += 1
            if self.desno==True and self.is_walking==True:
                spr(266 + 2*(round(self.spriteTimer)%2==0),int(self.x) - int(pogled.x),int(self.y) - int(pogled.y),6,1,0,0,2,2)
            elif self.desno==False and self.is_walking==True:
                spr(266 + 2*(round(self.spriteTimer)%2==0),int(self.x) - int(pogled.x),int(self.y) - int(pogled.y),6,1,1,0,2,2)
            else:
                spr(266,int(self.x) - int(pogled.x),int(self.y) - int(pogled.y),6,1,int(self.desno==False),0,2,2)
            
            
    def JetpackJoyride(self):
        if self.jetpackGorivo > 0:
            self.vsp = -self.jetpackJacina
            self.jetpackGorivo = self.jetpackGorivo - 1
            self.skok = 0
     
    def Pogoden(self, dmg):
        self.health -= dmg
        self.hitVar = 0
        if self.health < 0:
            print("HP MANJI OD 0")



#lista projektila
projectiles = []

class Enemy:
  x = 90 
  y = 90
  width = 16
  height = 16
  sprite = 1  
  dx = -1  
  vsp = 0
  gravitacija = 0.3
  skokJacina = 3
  minY = 120
  desno = False
  shotTimer = 0  # timer za pucanje
  shotFreq = 2 # koliko cesto puca
  coll = []

  def __init__(self, x, y):
    tile_size = 8
    self.x = x*tile_size
    self.y = y*tile_size

  def movement(self, coll):
    self.coll = coll
    self.x = self.x + self.dx
    if self.ProvjeriKolizije(6*self.dx, 0):
      if not self.ProvjeriKolizije(3*self.dx, -9):
        if self.ProvjeriKolizije(0, 1):
          self.vsp = -self.skokJacina
        else:
          self.dx = -self.dx
          self.desno = not self.desno
    elif self.ProvjeriKolizije(3*self.dx, 0):
      self.dx = -self.dx
      self.desno = not self.desno
    if self.x <= 0:
      self.dx = 1  # mijenja stranu kad takne lijevu stranu
      self.desno = True
    elif self.x >= pogled.ogranicenjeX:
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

    # puca svakih dvije sekunde
    if self.shotTimer >= 60 * self.shotFreq:
      self.shootProjectile()  # poziv funkcije za pucanje
      self.shotTimer = 0  # resetiranje timera

    #crtanje samog sebe
    if self.desno==True:
      spr(320,int(self.x) - int(pogled.x),int(self.y) - int(pogled.y),6,1,0,0,2,2)
    else:
      spr(320,int(self.x) - int(pogled.x),int(self.y) - int(pogled.y),6,1,1,0,2,2)

  def shootProjectile(self):
    projectile = Projectile(self.x + 5, int(self.y)) 

    projectile.desno = self.desno
    # doda projektil u listu
    projectiles.append(projectile)

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

class Projectile:
  x=0
  y=0
    
  width=4
  height=4
  
  def __init__(self, x, y):  # konstruktor klase
    self.x = x
    self.y = y
    self.dx = 1 
    self.dy = 0
    self.speed = 5  # brzina projektila
    self.desno = True
    self.width = 4
    self.height = 4
  
  def movement(self):
    if self.desno == True:
      self.x = self.x + self.speed
    else:
      self.x = self.x - self.speed

    #crtanje sebe
    spr(104, self.x - int(pogled.x), self.y - int(pogled.y), 0, 1, 0, 0, 1, 1)

      
  def MetakCheck(metak, colls):
            metak.coll=colls
            # metak se unisti
            if metak.x < 0 or metak.x > pogled.ogranicenjeX or Projectile.ProvjeriKolizije(metak, 0, 1):
                if metak in projectiles:
                    projectiles.remove(metak)
                    del metak
                else:
                    del metak
            elif metak.x < player.x + player.width and metak.y < player.y + player.height and metak.x > player.x - player.width + 8 and metak.y > player.y - player.height:
                if metak in projectiles:
                    print("Player pogoen", 80, 50)
                    player.Pogoden(player, 1) # damage ovdje ide ako cemo ga mijenjati 
                    projectiles.remove(metak)
                    del metak
                else:
                    del metak
            # ako je pogoden player (elif)
              
    
  # 1-2.-3 5---8.---11
    
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
     


class menu:
    m_ind=0

    def Menu():
        global state
        cls(0)
        menu.AnimateFrame()
        menu.AnimateTitle()

        # Opcije menija
        rect(1,48+10*menu.m_ind,238,10,2)
        print('Play', 100, 50, 4, False, 1, False)
        print('Quit', 100, 60, 4, False, 1, False)

        #  Šetanje po opcijama na meniju
        if btnp(1) and 48+10*menu.m_ind<50: #ako se budu dodavale još koje opcije, promijeniti uvijet
            menu.m_ind += 1
        elif btnp(0) and 48+10*menu.m_ind>=50:
            menu.m_ind += -1

        # Odabir 
        if key(48) and menu.m_ind==0:
            state = 'game'
            ZapocniLevel(level)
        elif key(48) and menu.m_ind==1:
            exit()

    def AnimateTitle():
        if(time()%500>250):
            print('NEON ESCAPE', 57, 20, 6, False, 2, False)
        elif(time()%500>150):
            print('NEON ESCAPE', 57, 20, 2, False, 2, False)
        elif(time()%500>350):
            print('NEON ESCAPE', 57, 20, 3, False, 2, False)
        elif(time()%500>550):
            print('NEON ESCAPE', 57, 20, 10, False, 2, False)

    def AnimateFrame():
        if(time()%500>250):
            rectb(0,0,240,136,6)
        elif(time()%500>150):
            rectb(0,0,240,136,2)
        elif(time()%500>350):
            rectb(0,0,240,136,3)
        elif(time()%500>550):
            rectb(0,0,240,136,10)


def lerp(a, b, t):
    return (1-t)*a + t*b

class Pogled:
    x = 0
    y = 0
    w = 240
    h = 136
    ograniceno = False
    ogranicenjeX = 0

    def __init__(self):
        self.postaviOgranicenja(240*8) # maks velicina levela

    def prati(self, objekt):
        self.x = objekt.x - (self.w - objekt.width)/2
        #self.y = objekt.y - (self.h - objekt.height)/2

    def postaviOgranicenja(self, maxX):
        self.ograniceno = True
        self.ogranicenjeX = maxX

    def pratiIgraca(self):
        lerpSnaga = 0.05
        lerpSnagaHoda = 0.2
        ispredStoji = 6
        ispredHoda = 16
        if player.is_walking:
            self.x = lerp(self.x, player.x - (self.w - player.width)/2 + ispredHoda*int(player.desno == True) - ispredHoda*int(player.desno == False), lerpSnagaHoda)
        else:
            self.x = lerp(self.x, player.x - (self.w - player.width)/2 + ispredStoji*int(player.desno == True) - ispredStoji*int(player.desno == False), lerpSnaga)

        if self.ograniceno:
            self.x = min(max(0, self.x), self.ogranicenjeX - self.w)

pogled = Pogled()



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
    explLenght = 1
    explSize = 16
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
    
    explosive=False
    explVar = 0
    explSizeVar = 2
    
    spr=378
    coll = []
    
    
    
    def MetakCheck(metak, colls):
            metak.coll=colls
            if metak.x < 0 or metak.x > pogled.ogranicenjeX or Metak.ProvjeriKolizije(metak, 0, 1):
                if metak in metci:
                    # za rakete i ekpslozije
                    if metak.explosive and metak.explVar < trecaPuska.explLenght * 60:
                        metak.speed = 0
                        metak.explVar += 1
                        metak.explSizeVar += int(metak.explVar / 5)
                        
                        minSize = min(metak.explSizeVar, trecaPuska.explSize)
                        
                        rect(int(metak.x) - int(pogled.x) - int(minSize / 2) + 2, int(metak.y) - int(pogled.y) - int(minSize / 2) + 2, minSize, minSize, 3)
                    else:
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
    
    svespr = [360, 361, 376]
    
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
        player.shootTimer=Puska.svep[Puska.p[Puska.tp]].firerate * 60
    
    
    def PromijeniPusku():
        if Puska.p[0] == Puska.p[Puska.tp]:
            Puska.tp = 1
        else:
            Puska.tp = 0
    
    
    def Pucanje():
      if player.shootTimer < 0:
        if key(6):
            Puska.pucaj(prvaPuska)
        if keyp(19):
            Puska.PromijeniPusku()
      
      eksdes = 12
      ekslijevo = -4
      eksGori = 6
      fliph = 0
      
      # gdje i kako ce se puska renderati
      if player.desno:
        Puska.x = int(player.x) + eksdes
        Puska.y = int(player.y) + eksGori
      else:
        Puska.x = int(player.x) + ekslijevo
        Puska.y = int(player.y) + eksGori
        fliph = 1
    
    
      spr(int(Puska.svespr[Puska.p[Puska.tp]]), Puska.x - int(pogled.x), Puska.y - int(pogled.y), 0,1,fliph,0,1,1)
    
      player.shootTimer = player.shootTimer - 1
        
      for metak in metci:
          
            if metak.explosive:
                spr(metak.spr + (int(metak.x) % 2),metak.x - int(pogled.x),metak.y - int(pogled.y),0,1,0,0,1,1)
            else:
                spr(metak.spr,metak.x - int(pogled.x),metak.y - int(pogled.y),0,1,0,0,1,1)
            
            if metak.desno == True:   
                metak.x = metak.x + metak.speed
            else:
                metak.x = metak.x - metak.speed

            
class PromjenaPuska:
    puskaBr = 2
    puskaSpr = 376
    x = 100
    y = 100
    
    pickUpBool = True
    
    def __init__(self, x, y, puskaBr = 2): # uzima x, y i broj puske (opcionalno)
        tile_size = 8
        self.x = x*tile_size
        self.y = y*tile_size
        self.puskaBr = puskaBr
        self.puskaSpr = Puska.svespr[puskaBr]
    
    def PickUp(self):
        spr(self.puskaSpr, int(self.x) - int(pogled.x), int(self.y) - int(pogled.y), 0,1,0,0,1,1)
        
        if self.pickUpBool and self.x < player.x + player.width and self.y < player.y + player.height and self.x > player.x - player.width + 8 and self.y > player.y - player.height:
            #zamijeni puske
            self.puskaSpr = Puska.svespr[Puska.p[Puska.tp]]
            noviBr = self.puskaBr
            self.puskaBr = Puska.p[Puska.tp] 
            Puska.p[Puska.tp] = noviBr
            self.pickUpBool = False
        elif not (self.x < player.x + player.width and self.y < player.y + player.height and self.x > player.x - player.width + 8 and self.y > player.y - player.height):
            self.pickUpBool = True

def test( a, b ):
    return a+b

player_starting_positions = [ # pocetna pozicija igraca za svaki level (u map editoru se prikazuje):
    [7, 12], # level 0
    [5, 28], # level 1
    [10, 44], # level 2
    [3, 63], # level 3
    [3, 72] # nepostojeci opet peti level
]
level_finish_tile_indexes = [ # indexi tileova sa vratima za zavrsetak levela
    50, 51, 52, 
    66, 67, 68, 
    82, 83, 84,
    211, 212, 213, 
    227, 228, 229, 
    243, 244, 245
]
background_tile_indexes = [ # indexi tileova sa elementima koji nemaju definiraju koliziju (pozadinski elementi)
	69, 70, 71, 
	56, 57, 58, 72, 73, 74, 
	85, 86, 87, 
	102, 103,
    88, 89, 90, 
    118, 119, 120, # zuti stol, no ima problem jer neki leveli koriste sredinu stola za platformu
    48, 49, 64, 65, 80, 81, 96, 97, # ljestve
    104, 11, 30
]
enemies = [ # pocetne pozicije enemyja za svaki level (u editoru se ispisuje koja)
    [Enemy(7, 12), Enemy(20, 13)], # level 0
    [], # level 1
    [Enemy(139, 46), Enemy(74, 46)], # level 2
    [Enemy(64, 62)] # level 3
]
pickups = [ # pocetna pozicija pick up pusaka za svaki level (u editoru se ispisuje koja)
    [PromjenaPuska(10, 4)], # level 0
    [], # level 1
    [PromjenaPuska(138, 39, 0), PromjenaPuska(74, 39)], # level 2
    [] # level 3
]

# sljedece varijable NE MIJENJATI:
LEVEL_HEIGHT = 17

def ZapocniLevel(level): # poziva se u menu.py kada se odabere opcija da se uđe u level
    tile_size = 8
    starting_pos = player_starting_positions[level]
    player.x = starting_pos[0]*tile_size
    player.y = (starting_pos[1] - LEVEL_HEIGHT*level)*tile_size
    pogled.x = max(0, player.x - (pogled.w - player.width)/2)
    player.hsp = 0
    player.vsp = 0

def IgrajLevel():
    cls(0)
    map(0, level*LEVEL_HEIGHT, 240, 18, -int(pogled.x), -int(pogled.y), 0)
    HUD()
    tile_size = 8
    levelEnemies = enemies[level]
    for enemy in levelEnemies:
        while (enemy.y > LEVEL_HEIGHT*tile_size):
            enemy.y -= LEVEL_HEIGHT*tile_size
    collidables = DefinirajKolizije([player, levelEnemies, metci, projectiles], level, LEVEL_HEIGHT)
    for enemy in levelEnemies:
        enemy.movement(collidables)
    for projektil in projectiles:
        projektil.movement()
        Projectile.MetakCheck(projektil, collidables)
    Puska.Pucanje()
    player.PlayerKontroler(player, collidables)
    pogled.pratiIgraca()
    for metak in metci:
        Metak.MetakCheck(metak, collidables)
    for metak in projectiles:
        Projectile.MetakCheck(metak, collidables)
    levelPickups = pickups[level]
    for pickup in levelPickups:
        while (pickup.y > LEVEL_HEIGHT*tile_size):
            pickup.y -= LEVEL_HEIGHT*tile_size
        pickup.PickUp()
    ProvjeravajJeLiIgracKodVrata()

def ProvjeravajJeLiIgracKodVrata(): # sluzi za kraj levela
    tile_size = 8
    kojiTile = mget(round(player.x/tile_size), round(player.y/tile_size) + level*LEVEL_HEIGHT)
    if kojiTile in level_finish_tile_indexes:
        ZavrsiLevel()

def ZavrsiLevel():
    global level
    level = level + 1
    ZapocniLevel(level)

def HUD():
    rect(0, 0, 110, 8, 0)
    print("Level:" + str(level), 1, 1, 12, True, 1, False)
    # Prikaz zivota
    spr(364, 50, 0, 6, 1, 0, 0, 1, 1)
    rect(60, 1, player.health*10, 5, 6)
    if player.health > 0:
        rect(60+player.health*10, 1, 30-player.health*10, 5, 3)
        print(str(player.health) + "HP", 92, 1, 12, True, 1, False)
    else: 
        print("0HP", 142, 1, 12, True, 1, False)
    # Prikaz puske i metaka
    rect(0, 8, 100, 8, 0)
    spr(Puska.svespr[Puska.p[Puska.tp]], 50, 8, 6, 1, 0, 0, 1, 1)
    print("Ammo: 5", 1, 8, 12, True, 1, False)
# <TILES>
# 001:8888888888888888888888888888888888888088888888888888888888888888
# 002:9999999999999999999999999999999999999999999999999999999999999999
# 003:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
# 004:eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
# 005:dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
# 006:00dddddd0deeeeeedeeeeeeedeeeeeeedeeeeeeedeeeeeee0deeeeee00dfffff
# 007:ddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffff
# 008:dddddf00eeeeeef0eeeeeeefeeeeeeefeeeeeeefeeeeeeefeeeeeef0ffffff00
# 009:dddddddfdeeeeeefdeeeeeefdeeeeeefdeeeeeefdeeeeeefdeeeeeefdfffffff
# 010:dddddddfdeeeeeefdedeefefdeeeeeefdeeeeeefdedeefefdeeeeeefdfffffff
# 011:dddddddddd9eafa8d9eafad8deafad98dafad9e8dfad9ea8dad9eaf8d8888888
# 012:00dddddd0deeeeeedeedeeeedeeeeeeedeeeeeeedeedeeee0deeeeee00dfffff
# 013:ddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffff
# 014:dddddf00eeeeeef0eeeefeefeeeeeeefeeeeeeefeeeefeefeeeeeef0ffffff00
# 015:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 016:dddddddddeeeeeeededdeeeededdeeeedeeeeeeedeeeeeeedeeeeeeedeeeeeee
# 017:ddddddddeeeeeeefeeeeffefeeeeffefeeeeeeefeeeeeeefeeeeeeefeeeeeeef
# 018:ffffffffffeeeeeefefeeeeefeefeeeefeeefeeefeeeeffffeeeeff2feeeef2f
# 019:ffffffffeeeeeeffeeeeefefeeeefeefeeefeeeffffeeeef2ffeeeeff2feeeef
# 020:000ddddd00deeeef0deeeeefdeeeeeefdeeeeeefdeeeeeefdeeeeeefdfffffff
# 021:ddddf000feeeef00feeeeef0feeeeeeffeeeeeeffeeeeeeffeeeeeefffffffff
# 022:000ddddd00deeeee0deeeeeedeeeeeeedeeeeeeedeeeeeeedeeeeeeedeeeeeee
# 023:ddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
# 024:ddddf000eeeeef00eeeeeef0eeeeeeefeeeeeeefeeeeeeefeeeeeeefeeeeeeef
# 025:000ddddd00deeeee0deeddeedeeeddeedeeeeeeedeeeeeeedeeeeeeedeeeeeee
# 026:ddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
# 027:ddddf000eeeeef00eeffeef0eeffeeefeeeeeeefeeeeeeefeeeeeeefeeeeeeef
# 028:3333333333444444343444443443444434443444344443443444443434444443
# 029:3333333344444433444443434444344344434443443444434344444334444443
# 030:8888888888bbbb888b8bb8b88bb88bb88bb88bb88b8bb8b888bbbb8888888888
# 031:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 032:deeeeeeedeeeeeeedeeeeeeedeeeeeeededdeeeededdeeeedeeeeeeeffffffff
# 033:eeeeeeefeeeeeeefeeeeeeefeeeeeeefeeeeffefeeeeffefeeeeeeefffffffff
# 034:feeeef2ffeeeeff2feeeeffffeeefeeefeefeeeefefeeeeeffeeeeeeffffffff
# 035:f2feeeef2ffeeeeffffeeeefeeefeeefeeeefeefeeeeefefeeeeeeffffffffff
# 036:dfffffffdeeeeeefdeeeeeefdeeeeeefdeeeeeef0deeeeef00deeeef000fffff
# 037:fffffffffeeeeeeffeeeeeeffeeeeeeffeeeeeeffeeeeef0feeeef00fffff000
# 038:deeeeeeedeeeeeeedeeeeeeedeeeeeeedeeeeeee0deeeeee00deeeee000fffff
# 039:eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffff
# 040:eeeeeeefeeeeeeefeeeeeeefeeeeeeefeeeeeeefeeeeeef0eeeeef00fffff000
# 041:deeeeeeedeeeeeeedeeeeeeedeeeddeedeeeddee0deeeeee00deeeee000fffff
# 042:eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffff
# 043:eeeeeeefeeeeeeefeeeeeeefeeffeeefeeffeeefeeeeeef0eeeeef00fffff000
# 044:3444444334444434344443443444344434434444343444443344444433333333
# 045:3444444343444443443444434443444344443443444443434444443333333333
# 046:3333333333444433343443433443344334433443343443433344443333333333
# 047:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 048:dddddddddd000000dddddddddd000000dddddddedd000000dddddeeedd000000
# 049:dddeeeee000000eedeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000ee
# 050:dddddddddeeeeeeedeeeeeeedeeeeeeedeeeffffffefddedffefdedddeefedde
# 051:ddddddddeeeeeeeeeeeeeeeeeeeeeeeeffffffffdeeddddeeeddddededdddedd
# 052:dddddddfeeeeeeefeeeeeeefeeeeeeefffffeeefddddfeffdddefeffddeefeef
# 053:00aaaaaa0aaaaaaaa8888888a8aa8aa8a8aa8aa8a88888880a88888800aaaaaa
# 054:aaaaaaaaaaaaaaaa88888888aa8aa8aaaa8aa8aa8888888888888888aaaaaaaa
# 055:aaaaaa00aaaaaaa08888888a8aa8aa8a8aa8aa8a8888888a888888a0aaaaaa00
# 056:0000000800000084000008440000844400084444008444480888888084884800
# 057:8888800083384800833844808888444880084448000088880000088800000008
# 058:000000000000000000000000800000008000000088888800eeeee880e8888e88
# 059:2222222222222222222222222222222222222222222222222222222222222222
# 060:3333333333333333333333333333333333333333333333333333333333333333
# 061:4444444444444444444444444444444444444444444444444444444444444444
# 062:1111111111111111111111111111111111111111111111111111111111111111
# 063:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 064:dddeeeeedd000000ddeeeeeede000000deeeeeeede000000deeeeeeede000000
# 065:eeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000ee
# 066:deefddeedeefdeeddeeeffffdeeeeeeedeeeeeeedeeddddddeedeeeedeedeeee
# 067:ddddeddddddeddddffffffffeeeeeeeeeeeeeeeeddddddddeeeeeeeeeeeeeeee
# 068:deedfeefeeddfeefffffeeefeeeeeeefeeeeeeefddddfeefeeeefeefeeeefeef
# 069:ddddddddd77777770f77777700ffffff0007f0000007f0000007f0000007f000
# 070:dddddddd7777777777777777ffffffff00000000000000000000000000000000
# 071:dddddddd7777777f777777f0ffffff000007f0000007f0000007f0000007f000
# 072:8888880084884800888888800844444800844444000844440008444400888888
# 073:0000000800000008000000080000000880000000800000008000000088000000
# 074:e80008e8e8000080e8000000ee8000008ee80000088000000000000000000000
# 075:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# 076:7777777777777777777777777777777777777777777777777777777777777777
# 077:6666666666666666666666666666666666666666666666666666666666666666
# 078:5555555555555555555555555555555555555555555555555555555555555555
# 079:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 080:eeeeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000
# 081:eeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000ee
# 082:deedeeeeffedeeeeffedeeeedeedeeeedeedffffdeeeeeeedeeeeeeedfffffff
# 083:eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffeeeeeeeeeeeeeeeeffffffff
# 084:eeeefeefeeeefeffeeeefeffeeeefeeffffffeefeeeeeeefeeeeeeefffffffff
# 085:ddddddddd33383330f33383300ffffff0003f0000003f0000003f0000003f000
# 086:dddddd8d8333383333333833ffffffff00000000000000000000000000000000
# 087:dddddddf3333333f333833f0ffffff000003f0000003f0000003f0000003f000
# 088:00888888ddeeeeefddeeeeeeddeeeeeeddeeeeeeddeeeeeeddeeeeeeddeeeeee
# 089:88000000ffff0000ffff0000ffff0000ffff0000ffff0000ffff0000ffff0000
# 090:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 091:ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
# 092:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 093:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 094:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 095:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 096:eeeeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000
# 097:eeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000ee
# 098:ddf00000deef0000deeedddddeeeeeeedeeeeeeedeeeffffdeef0000dff00000
# 099:0000000000000000ddddddddeeeeeeeeeeeeeeeeffffffff0000000000000000
# 100:0000000000000000ddddddddeeeeeeeeeeeeeeeeffffffff0000000000000000
# 101:00000ddf0000deefddddeeefeeeeeeefeeeeeeefffffeeef0000deef00000dff
# 102:0000004800000848000088400004440000088000000880000084480008888880
# 103:8000000088bb000088bbb000bbbbb0000bbbb000000000000000000000000000
# 104:ddddddd8dbbbbbb8d9999998dbbbbbb8d9999998dbbbbbb8d9999998d8888888
# 105:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 106:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 107:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 108:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 109:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 110:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 111:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 112:888888888fffffff8fff22228222ff3382ff333f8f3333ff83322fff8fff2222
# 113:88888888ffffff33223333ff33ff2222fffff3fff3333fff3ffffff222f22f2f
# 114:8888888833333338fff3fff8233f33f822222228fffff33822fffff8ff2ffff8
# 115:ffffffffffeeeeeefefeeeeefeefeeeefeeefeeefeeeeffffeeeeff5feeeef5f
# 116:ffffffffeeeeeeffeeeeefefeeeefeefeeefeeeffffeeeef5ffeeeeff5feeeef
# 118:ddddddddd44444440f44444400ffffff0004f0000004f0000004f0000004f000
# 119:dddddddd4444444444444444ffffffff00000000000000000000000000000000
# 120:dddddddd4444444f444444f0ffffff000004f0000004f0000004f0000004f000
# 121:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 122:eaeeeeeeeaaeeeaeeeeaeeaeeaeaeaaeeaaaaaeeeeeaaeeeeaaaaaaaeeeaeeee
# 123:eeeeeebbeeeeeeebeeeeeeeeeeeeebbeeebeeebeebbebebbbbbebebbbbeebeeb
# 124:bbbbbbbbbbbbbbbbbbbbbbbbebbeebbbeeeeebbeeeeeeeeeeeeeeeeeeeeeeeee
# 125:bbbbbbeeeeebbeeebeeeeeeebbbbeeeebbbbeeeebbbbbeeebbbbeeeebeeeeeee
# 126:eeeeebbbeeeebbbbeeeeebbbeeeeeebbebeebbbbebbeebbbbbbeeebbbbbbeeeb
# 127:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 128:82fff3ff832333ff8ff2fff28fff222f8f33333f83fffff38fffffff88888888
# 129:ff2ff2ffffffffff2ffffff32f22233ff2ff22fffff3322f3333ff2288888888
# 130:fff22ff8fffff2f833fffff8ff33f228ffff2ff8fff2f3f8ff2fff3888888888
# 131:feeeef5ffeeeeff5feeeeffffeeefeeefeefeeeefefeeeeeffeeeeeeffffffff
# 132:f5feeeef5ffeeeeffffeeeefeeefeeefeeeefeefeeeeefefeeeeeeffffffffff
# 133:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 134:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 135:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 136:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 137:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 138:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 139:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 140:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 141:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 142:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 143:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 144:ddddddddd34444440ff43434000fffff00000000000000000000000000000000
# 145:dddddddd4444444434343434ffffffff00000000000000000000000000000000
# 146:dddddddd4444443d34343ff0fffff00000000000000000000000000000000000
# 147:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 148:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 149:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 150:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 151:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 152:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 153:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 154:beeebeebbbeebbbeebeebbeeeebbbbeeeeebbbbeeebbbeebebebbbeebeebeebe
# 155:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 156:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 157:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 158:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 159:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 160:0000000088888888888888888888888888888888888880888888888888888888
# 161:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 162:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 163:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 164:4444444444444440444444004444400044440000444000004400000040000000
# 165:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 166:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 167:4444444404444444004444440004444400004444000004440000004400000004
# 169:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 170:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 171:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 172:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 173:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 174:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 175:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 176:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 177:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 178:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 179:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 180:4444444404444444004444440004444400004444000004440000004400000004
# 181:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 182:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 183:4444444444444440444444004444400044440000444000004400000040000000
# 184:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 185:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 186:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 187:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 188:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 189:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 190:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 191:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 192:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 193:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 194:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 195:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 196:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 197:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 198:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 200:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 201:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 202:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 203:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 204:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 205:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 206:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 207:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 208:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 209:3333333343333333443333334443333344443333444443334444443344444443
# 210:3333333333333334333333443333344433334444333444443344444434444444
# 211:eeeeeeeeefffffffef000000ef000000ef002222ef002222ef002222ef002222
# 212:eeeddeeefffddfff000dd000000dd000200dd002200dd002200dd002200dd002
# 213:eeeeeeeefffffffe000000fe000000fe222200fe222200fe222200fe222200fe
# 215:2222222232222222332222223332222233332222333332223333332233333332
# 216:2222222222222223222222332222233322223333222333332233333323333333
# 217:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 218:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 219:e0000000e0000000e0000000e0000000e0000000e0000000e0000000e0000000
# 220:0000000e0000000e0000000e0000000e0000000e0000000e0000000e0000000e
# 221:e00ddddde00ddddde0000000e0000000e0000000e0000000e0000000e0000000
# 222:d00ee00dd00ee00d000ee000000ee000000ee000000ee000000ee000000ee000
# 223:ddddd00eddddd00e0000000e0000000e0000000e0000000e0000000e0000000e
# 224:667ee77c76676777777776676766776e77676777ee7666677ee77ede677e777c
# 225:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 226:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 227:ef000000ef000000ef000000ef000000ef000000ef000000ef000000ef000000
# 228:000dd000000dd000000dd000044dd440044dd440000dd000000dd000000dd000
# 229:000000fe000000fe000000fe000000fe000000fe000000fe000000fe000000fe
# 231:000ee000000ee00000edce0000edce000edddce00edddce0eedddceeedddddce
# 232:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 233:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 234:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 235:e0000000e0000000e0000000e0000000e0000000e0000000e0000000e0000000
# 236:0000000e0000000e0000000e0000000e0000000e0000000e0000000e0000000e
# 237:e0000000e0000000e0000000e0000000e0000000e0000000e0000000e00fffff
# 238:000ee000000ee000000ee000000ee000000ee000000ee000000ee000f00ee00f
# 239:0000000e0000000e0000000e0000000e0000000e0000000e0000000efffff00e
# 240:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 241:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 242:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 243:ef000000ef000000ef000000ef000000ef000000ef000000efffffffeeeeeeee
# 244:000dd000000dd000000dd000000dd000000dd000000dd000fffddfffeeeddeee
# 245:000000fe000000fe000000fe000000fe000000fe000000fefffffffeeeeeeeee
# 247:eddddddeeddddddeeddddddeeddddddeeddddddeeddddddeeddddddeeeeeeeee
# 248:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 249:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 250:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
# 251:e0000000e0000000e0000000e0000000e0000000e0000000e0000000e0000000
# 252:0000000e0000000e0000000e0000000e0000000e0000000e0000000e0000000e
# 253:e0000000e00fffffe0000000e00fffffe0000000e0000000eeeeeeeeeeeeeeee
# 254:000ee000f00ee00f000ee000f00ee00f000ee000000ee000eeeeeeeeeeeeeeee
# 255:0000000efffff00e0000000efffff00e0000000e0000000eeeeeeeeeeeeeeeee
# </TILES>

# <SPRITES>
# 000:666666006666600566600055660011116605055466000544666000446600e154
# 001:0006666655006666555006661111066644040666440406664444066644440666
# 002:600066006050600560000055666011116660555466605544666000546660ee15
# 003:0006666655006666555006661111066644040666440406664444066644440666
# 004:666666006000600560500055600011116660555466605544666000546660ee15
# 005:0006666655006666555006661111066644040666440406664444066644440666
# 006:666666006000600560500055600011116660555466605544666000546660ee15
# 007:0006666655006666555006661111066644040666440406664444066644440666
# 008:666666006000600560500055600011116660555466605544666000546600ee15
# 009:0006666655006666555006661111066644040666440406664444066644440666
# 010:6666660066666002666000226600222266020222660002226660002266002222
# 011:0006666622006666222006662222066622020666220206662222066622220666
# 012:6666660060006002602000226000222266602222666022226660002266602222
# 013:0006666622006666222006662222066622020666220206662222066622220666
# 016:660eee15600ee0e160ee0eee6044000060000eee6660ee00660ee00666000066
# 017:55500666eee00666110e0666001ee066eee040660ee0066660ee066660000666
# 018:6660ee016600e0ee660440ee660000006660eee0660ee0066600006666666666
# 019:555000661ee04066e10ee066000006660eee0066600ee0666600006666666666
# 020:6660ee016600e0ee660ee0ee66044000660000ee6660ee00660eee0666000066
# 021:555000661ee04066e10ee0660011e066eee006660ee0066660ee066660000666
# 022:660eee01660ee00e660eee406660ee40666000006660eee06660ee0066600006
# 023:555066661ee06666e10e666600116666eee06666ee0066660ee0666600006666
# 024:66000e0160ee0ee060ee0eee60440ee06600eeee6660ee00660eee0666000066
# 025:5550006600004066ee0e4066eeee4066000006660ee0066660ee066660000666
# 026:6602222260022022602202226022000060000222666022006602200666000066
# 027:2220066622200666220206660022206622202066022006666022066660000666
# 028:6660220266002022660220226602200066000022666022006602220666000066
# 029:2220006622202066220220660022206622200666022006666022066660000666
# 032:6000660060206002600000226660222266602222666022226660002266602222
# 033:0006666622006666222006662222066622020666220206662222066622220666
# 034:6666666066666605666660556666011160060555044015550ee015550eeee155
# 035:0006666655006666555066661111066655550666555506665555066655550006
# 036:666666606666660566666055666601116666055566601555600015550440e155
# 037:0006666655006666555066661111066655550666555500065555044055550ee0
# 038:66666000666600556600055560011111605055446000544466000444600e1544
# 039:0066666650066666550066661110666640406666404066664440666644406666
# 040:66666000666600556600055560011111605055446000544466000444600e1544
# 041:0066666650066666550066661110666640406666404066664440666644400000
# 042:66666000666600556600055560011111605055446000544466000444600e1544
# 043:0066666650066666550066661110666640406666404066664440666644406666
# 044:666666fe66666fee6666feee6666feee66666fee666666fe66600e0066fee034
# 045:d6666666ed66666622d66666eed66666ed666666e66666660e00666640ed6666
# 048:6660220266002022660220226600000066602220660220066600006666666666
# 049:2220006622202066220220660000066602220066600220666600006666666666
# 050:600eee15660ee0e166000eee6666000066600eee6660eee0660ee00666000066
# 051:55e00440eee0eee0110eee0000110066eee0066600ee06666000066666666666
# 052:0eeeee15600ee0e1660eeeee666000006660eeee660ee0006600006666666666
# 053:55e0eee0eee0ee06110ee00600110666eee066660ee0066660ee066660000666
# 054:60eee15500ee0e1e0ee0eee1044000000000eeee660ee00060ee006660000666
# 055:55006006e000022000422400ee420066ee000666ee0066660ee0666600006666
# 056:60eee15500ee0e1e0ee0eee1044000000000eeee660ee00060ee006660000666
# 057:55003330e000030000430930ee439300ee000006ee0066660ee0666600006666
# 058:60eee15500ee0e1e0ee0eee1044000000000eeee660ee00060ee006660000666
# 059:55006006e0000aa0004aa5aaee4a5aaaee00aa00ee0000660ee0666600006666
# 060:66feee0366feffe066fe6fe066fe6eee666ffee66666fe666666fe666666fff6
# 061:0eeed666ef6ee666ee6ee666ed66e666fed66666fee66666fee666666fee6666
# 064:666666fe66666fee6666feee6666ffee66666ffe666666ff66600e0066fee034
# 065:d6666666ed66666622d66666eed66666ed666666e66666660e00666640eed666
# 066:666666fe66666fee6666feee6666ffee66666ffe666666ff66666ee066666e03
# 067:d6666666ed66666622d66666eed66666ed666666e66666660e66666640666666
# 068:666666fe66666fee6666feee6666ffee66666ffe666666ff66666ee066666e03
# 069:d6666666ed66666622d66666eed66666ed666666e66666660f66666630fefeff
# 070:6666ff66666feef666ffffee6feeffff6feef66666feeff7666feef766ffff7f
# 071:6666666666666666ef66666666666666666666667dd66666fffd6666222f6666
# 072:6666ff66666feef666ffffee6feeffff6feef66666feeff7666feef766ffff7f
# 073:6666666666666666ef66666666666666666666667dd66666fffd6666233f6666
# 074:6666ff66666feef666feffee6fefffff6feef66666feefff666feef766ffff7f
# 075:6666666666666666ef666666666666666666666677d66666fffd6666233f6666
# 076:a6666888aaa68999a9989999a99999ff6a999fdd66a9fddd6699fd226699fd22
# 077:886666f69986fff6999888f6f99988f6df998f66ddf986662df9f6662df9f666
# 080:6feeee036fe6f0e06fee6fe066f66eee6666fee66666fe66666fee66666ffee6
# 081:0ee6ed66e0e6ee66ee66eed6ed666d66fed66666ffed66666ffd666666fed666
# 082:6666eee06666eeee6666efee66666ffe66666fee6666fee66666fe6666666ff6
# 083:0e666666e0666666ee666666ed666666fe666666ffe66666fee66666ff666666
# 084:6666eee06666eeee6666efee66666ffe66666fee6666fee66666fe6666666ff6
# 085:0effeff6eff6f666ee66f666ed666666fe666666ffe66666fee66666ff666666
# 086:66fee777666fe77766fee77766fe777f66fe777666fe77d6666fe77d666ffff7
# 087:f2fd66667f7d66667777666677776666f7776666fe7d66666fe7d6666ffedd66
# 088:66fee777666fe77766fee77766fe777766fe77776ffe77776fffeeee6ffffffe
# 089:f2fd66667f7d66667777666677776666766666667d66666677d66666e7766666
# 090:66fee777666fe777666fe777666fe77e66ffe77e66ffe7776feffeee6feefffe
# 091:f2f766667f776666777d666677d66666ed6666667edd6666777d6666ee776666
# 092:66a99fd266a999ff6a9a9999a9999888a9999986999999869999998669988866
# 093:df99f666f998f66699898f66889998f6899998f6899999f6899999f66888ff66
# 096:a6666a99aaa6a999aa9a9999aa9999ff6aa99fdd66a9fddd6699f2226699f222
# 097:886666f69986fff6999888f6f99998f6df998f66ddf98666ddf9f666ddf9f666
# 098:a6666a99aaa6a999aa9a9999aa9999ff6aa99fdd66a9fddd6699f2226699f222
# 099:886666f69986fff6999888f6f99998f6df998f66ddf98666ddf9f666ddf9f666
# 100:a6666888aaa68999a9989999a99999886a99982266a982236698223366982334
# 101:886666f69986fff6999888f6899988f628998f66228986663228f6663328f666
# 102:a6666888aaa68999a9989999a99999886a99982266a982336698233466982344
# 103:886666f69986fff6999888f6899988f628998f66328986663328f6664328f666
# 104:0000000000200000222222220242000002200000020000000000000000000000
# 105:0000000000444000400400003443444444f40400044004000400000000000000
# 106:0000000000000000444440440044440004000044444404400000000000000000
# 107:000000000000000000bbbbb00000000000bbbbb0000000000000000000000000
# 108:000000000cc00cc0c2cccc2cc22cc22cc222222ccc2222cc0cc22cc000cccc00
# 112:66a99f2d66a999ff6aaa9999aa999999a9999996999999866999886666666666
# 113:df99f666f999f66699998f66899998f6899998f6899999f6899999f66888ff66
# 114:66a99f2d66a999ff6aaa9999aa999999a9999986a99999869999998669998866
# 115:df99f666f999f66699998f66899998f6899999f6899999f66888ff6666666666
# 116:66a8223366a982236a9a8222a9999888a9999986999999869999998669988866
# 117:3228f6662289f66622898f66889998f6899998f6899999f6899999f66888ff66
# 118:66a8233466a982336a9a8222a9999888a9999986999999869999998669988866
# 119:3328f6663289f66622898f66889998f6899998f6899999f6899999f66888ff66
# 120:000000008855888e8888588e0868000008800000080000000000000000000000
# 122:0000000000000000002233000222333000223300000000000000000000000000
# 123:0000000000000000002332000223322000233200000000000000000000000000
# </SPRITES>

# <MAP>
# 006:000000000000006137472131810000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 007:000000000000006238482232820000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 011:000000000000000000000000000000000000000000000000011100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 012:000000000000000000000000000000000041510000000000021200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 013:00000000000000000000000000000000a090900000000091a1b100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 014:404040404040404040404000000000a0a090a00000000092a2b20000000000000000003d4d5d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 015:40404040404040404040404040404040404040404040404040404040404000000000003e4e5e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 016:40404040404040404040404040404040404040404040404040404040404000000000003f4f5f00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 017:000000000000900000000000000000000000000000000000000000000000001d001d00001d00000000001d00000000000000000000900b0b0b90000000000000000000000000000000000000000000000000000000000000000000000090900000000090900000009090000000000000000000000000000000000000000000000000000000001d0000001d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a900a900000000a9a9a90000000000a900a9000000000000000000000000000000000000
# 018:000000000000900000000000000000000000000000000000000000000000001d001d00001d00000000001d00000000000000000000900b0b0b900000000000000000000000000000000000000000000000000000000000000000000000909000000000a0a00000009090000000000000000000000000000000000000000000000000000000001d0000001d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a900a900000000a9a9a90000000000a900a9000000000000000000000000000000000000
# 019:000000000000900000000000000000000000000000000000000000000000001d001d00001d00000000001d00000000000000000000900b0b0b90000000000000000000000000000000000000000000000000000000000000000000000090900000000000000000009090000000000000000000000000000000000000000000000000000000001d0000001d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a900a900000000a900a90000000000a900a9000000000000000000000000000000000000
# 020:000000000000900000000000000000000000000000000000000000000000001d001d00001d00000000001d0000000000000000000062720b7282000000000000000000000000000000000000000000000000000000000000000000000090900000000000000000009090909090000000000000000000000000000000000000000000000000001d0000001d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a9a900a90000000000a900a9a90000000000000000000000000000000000
# 021:7b0000004190909051000000000000000000000000000000000000000000001d001d0000607070707070800000000000000000000000900b90000000000000000000000000000000000000000000000000000000000000000000000000909000000000000000000090900000000000000000000000000000000000000000000000000000006070707070708000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a90000000000000000000000000000000000000000003d4d5d0000
# 022:000000009000000090000000000000000000000000000000000000000000001d001d0000000000000000000000000000000000000000901b90000000000000000000000000000000000000000000000000000000000000000000000000909000000000000000000090900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000060707070800000000000000000000000000000000000000000000000000000003e4e5e0000
# 023:000000004200000052000000000000000000000000000000000000000000001d001d0000000000000000000000000000000000000000900b90000000000000000000000000000000000000000000000000000000000000a0a000000000909000000000a0a0000000909000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001d001d000000000000000000000060707070800000000000000000000000003f4f5f0000
# 024:0000000000000000000000000000000000000000000000000000000000000060708000000000000000000000000000000000000000900b0b1b90000000000000000000000000000000000000000000000000000000000090900000000090900000000090900000009090000000000000000000000000000000000000000090900e000e000e000e000e0e000e0e0e0e000090909090a90000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009090900313000000001d001d0000007e7ea9a900000000001d001d000000000000909090909090909090909090
# 025:00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000901b0b901b0b9000000000000000000000000000000090909090031300000000000000909000000000a0a0909000009090000000a0a0000000000000000000000000607070800000000090900d0e00000e0e0000000e0e0e0d0d0e0e0090909090a90000000000000000000000000000000000000000000000000000000000000000000000000000000000009090909090900414000000001d001d0000006070707080000000001d001d000000000000909090909090909090909090
# 026:000000000000000000000000000000000000000000000000a9a9a900000000000000000000000000000000000000000000000000901b1b901b1b900000000000000000000000000000909090011104140000000000000090900000000000000000000090900000000000000000000000000000000000001d1d000000000090900d0d0e000d0e000e000e0d0d0e0e0d0e0e90909090a9000000000000000000a7a7a7a7a7a7a700a7b0b0000000000000000000000000000000000000000000009086869090900515000000001d001d000000001d001d00000000001d001d000000000000909090909090909090909090
# 027:00000000000000000000000000000000000000000090909090909000000000000000000000000000000000000000000000000000900000900000900000000000000000000000000090909090021205150000000000000090900000000000000000000090900000000000000000000000000000000000001d1d000000000090900d0e0d0e0d0d0e0e000e0e0e0d0e0d0d0e90909090a900000000000000a7a700b0b0a7a700a7a7a7b0b0e2e200000000000000000000000000000000009090909086869090900616000000001d001d000000001d001d00000000001d001d000000000000909090909090909090909090
# 028:000000000000000000000000002131000000000000000000000000000000000000008393a300000000000000000000000000000090000090000090000000000000000000000000909021313747e106160000000000000090900000000000000000000090900000000000000000006070708000000000001d1d000000000090900e0d0e0d0e0e0e0d0e0d0d0e0e0e0e0d0e90909090a900000000000000a700b0b0b0b0b0000000b0b0b0e2e2e2000000000000000000000000000000009086869086869090900515000000001d001d000000001d001d00000000001d001d000000000000909090909090909090909090
# 029:0000000000000000000000000022320000000000cdddedfdddedfdbd0000000000008494a400000000000000000000000000000000000000000000000000000000000000009090909022323848e10515000000000000009090000000000000000090909090000000000000000000001d1d0000000000001d1d00000000009090909090909090909090909090909090909090909090a900000000000000b0b0b0b0b0b0b0b00000b0b0b0e2e2e2e200c7000000000000000000009090909086869086869090900616000000001d001d000000001d001d00000000001d001d000000000000909090909090909090909090
# 030:00a9a9a90000000000a700003747374700000000cedeeefedeeefebe0000000000008595b000000000000026560000000000000000000000000000000000000000000090909090902131374701110515000000000000009090000000000000009090909090000000000000000000001d1d0000000000001d1d00000000009090909090909090909090909090909090909090909090a7a7a7a7a7a7a7b0b0b0b0b0b0b0b0b07e7eb0b0b0e2e2e2e2e2e2e20000000000000000009086869086869086869090900515000000001d001d000000001d001d00000000001d001d000000000000909090909090909090909090
# 031:00a9a9a99090909090a7a7a93848384800000000cfdfefffdfefffbf000000000055656575000000005464646464740000000000000000000000000000000000009090909090909022323848021206160000000000000090907e7e00000000909090909090000000000000000000001d1d0000000000001d1d000000000090909090909090909090909090909090909090909090907e7e7e7e7e7e7eb0b0b0b0b0b0b0b0b07f7fb0b0b0e2e2e2e2e2e2e2e200000000000000009086869086869086869090900616000000001d001d000000001d001d00000000001d001d007e7e7e7e7e909090909090909090909090
# 032:9090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090a0a09090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090
# 033:909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090
# 034:000000000000000000007b8b7b8b00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 035:404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040
# 036:400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000040404040
# 037:400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000040404040
# 038:400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000263646562636465626364656263646562636465600000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000040404040
# 039:400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001110111011101110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000040404040
# 040:400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002120212021202120000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000040404040
# 041:4000000000000000000000000000000000000000000000000000c0d0e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c0d0e000000000c0d0e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c0d0e000000000c0d0e000000000000000000000000000000000000000000000000000000000c0d0e0000000000000c0d0e0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000040404040
# 042:400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000313909090909090909000000000000000000000000000909090909090909090900313000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000040404040
# 043:40000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000041440000000000000000000000000000000000000000000000000000000000040041400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000031390909090909090b3b3b3b3b3b3b3b3b39090909090b3b3b3b3b3b3b3b3b3b39090909003130000000000000000000000000040404040
# 044:40000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000051540b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b340031300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000041440b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b34004140000000000000000000000000040404040
# 045:4000000000000000000000000000000000000000000000000000000000000000006070800000607080000000000000000000000000000000000000000000000000008393a300000000000000000000000000000000000000061640b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b34004140000000000000000008393a300000000000000000000000000000000000000000000000000000000000000008393a30000000000000000000000000000051540b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b34005150000000000000000233343000040404040
# 046:4000000000000000004040400000000000000040404000000000667686000000000000000000000000000000000000011100000000004151000000000000000000008494a4b0b0b000000000000000000000000000000000051540b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b34005150000000000000000008494a461718100000000000000000000400000000000000000000000400000000000008494a4e100000000000000000000000000061640b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b34006160000000000000000243444000040404040
# 047:400000005565750040404040b3b3b3b3b3b3b340404040000000677787000000000000000000000000000000000000021200000000004252000000000000000000008595a567778700000000000000000000000000000000061640b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b34006160000000000000000008595a562728200000000000000000040400000000000000000000000404000000000008595546474000000000000000000000000061640b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b34006160000000000000000253545000040404040
# 048:404040404040404040404040b3b3b3b3b3b3b340404040404040404040404040b3b3b3b3b3b3b3b3b3b340404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b34040404040404040404040404040404040404040404040404040404040b3b3b3b3b3b3b3b3b3b3b3404040404040404040404040404040404040404040404040404040b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b34040404040404040404040404040404040404040
# 049:404040404040404040404040b3b3b3b3b3b3b340404040404040404040404040b3b3b3b3b3b3b3b3b3b340404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b34040404040404040404040404040404040404040404040404040404040b3b3b3b3b3b3b3b3b3b3b3404040404040404040404040404040404040404040404040404040b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b34040404040404040404040404040404040404040
# 050:404040404040404040404040b3b3b3b3b3b3b340404040404040404040404040b3b3b3b3b3b3b3b3b3b340404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b34040404040404040404040404040404040404040404040404040404040b3b3b3b3b3b3b3b3b3b3b34040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040
# 051:30302020201010102020203030c78233330000000000000000000000000000000000000000000000000000007ad3d3d3d31dc3c37db3b3b3b3b3b3b3b3b3b3b3b38dc3c32dd3d3d3d3d34aa0a00000a0a0000000a0a000000040120000404000000000000000000000000000000000000000000000000000000000000030303026364656263646562636465626364656263646562636465626364656263646562636465626364656263646562636465626364656101010101020202020202020202020101010101010101010202020202020202020202020101010101010101010101010101010203030303030303030
# 052:303030202020101010203030c782003434000000000000000000000000000000000000000000000000000000007ad3d3d3d3c3c3c3c37db3b3b3b3b3b3b3b38dc3c32dd3d3d3d3d3d34a00a0a00000a0a0000000a0a0000000401200004040000000000000000000000000000000000000000000000000000000000000403030000000000000000000000000000000000000000000000000000000000000000000646464646400000000000000000000000000001010101020202030c7c7c7c7c7302020101010101010101020303030303030303020202020101020202020101010102020202020c7c7c7c7c7c73030
# 053:30303030202020202030c7c782000033330000000000000000000000000000e10000e10000000000000000000000007ad3d31dc3c3c3c3c3c3c3c3c3c3c3c3c3c32dd3d3d3d3d34a000000a0a00000a0a000000040a000000012120000404000000000000000000000000000000000000000000000000000000000000040e730a300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020101010203030304040404040c730202020101010102030303030c740c7c7c7303030302020202030302020201020202030c74082e262404040c7c7
# 054:c7c730303030303030c7404000e1003434000000000000000000000000000021213131a30000000000000000000000007ad3d3d31dc3c3c3c3c3c3c3c3c3c3c32dd3d3d3d34a0000000000a040000040a0000000a0a0000000404000004090000000000000000000000000000000000000000000000000000000000919403030a4000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064646464202020202030404040b20040a940c73030202020202030303030c74040404040c7c7c7c7303030c7c73030302020202030c74082000919624040a940
# 055:4040c7c7c7c7c7c7c74040820009196282000000000000000000000000000022223232a400000000000000000000000000007ad3d3d31dc3c3c3c3c3c32dd3d3d3d3d34a00000000000000a04000004040000000a04000000062820000409000000000000061404040404019191919191919191919404040a3000000004040300000000000000000000000000000000000000000000000000000006464646464640000000064646400000000000000000000000030202020203040b200000092404040c7303030303030c7c7404040409240404040404040c7c7c74040c7c73030303030c74082000000000000624040
# 056:40a9404040404040404082e10000000000000000000000000000000000000010213110000000000000000000000000000000007ad3d3d31dc3c3c3c32dd3d3d3d3d34a0000000000000000a0a000006282000000404000000000000000409000000000614090909090404000000000000000000000404040a40000000040403000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c730302020304000e10000009240404040c7303030c7404040a940400092400092a9404040404040404040c7303030c7408200e20000000000006240
# 057:40404040820000624082192900000000000000000000000000000000000000102232000000000000000000000000000000000000007ad3d3d3d3d3d3d3d3d34a000000000000000000000040a000000000000000404000000000000000909000000919404090233343904000000000000000000000404040000000000040404000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006464646464640000403030303040b2646400000000009240404040c7c74040404040404000000000006240820000000062404040c7c7c740401919290000000000000062
# 058:0000000000000000000000000000000000000000000000000000000000001010213100000000000000000000000000000000000000007ad3d3d3d3d3d3d34a00000000000000000000000062820000000000000040400000000000000090400000000040409024344490400000000000000000000040404019290000004040400000000000000000000040404000000000000000006464646464640000000000000000000000000000000000000000000000000040c73040404000000000000000000092404040404040404040404082e20000000000000000000000e262404040404040820000000000000000000000
# 059:0000000000000000000000008393a30000008393a300000000000000001010102232000000000000008393a30000000000000000000000007ad3d3d34a00000000000000000000000000000000000000000000006282000000000000009090000000004040902535459040000000000000000000e2404040a3000000004040400000000000000000004040a9400000000000000000000000000000000000000000000000000000000000000000000000000000004040404040b200000000000000000000924037474040a940404082646400000000000000000000006464646240a94082000000000000000000000000
# 060:0000000000000000000000008494a40000008494a400000000000000002690909090905600000000008494a4000000000000000000000000007ad34a0000000000000000000000000000000000000000000000000000000000000000006282290000004040903030909040e20000000000000000b3404040a40000000040a9a900000000000000404040404030000064646464000000000000000000000000000000000000006464646464000000000000000000404040404000000000000000000000e10040384840404040408200000000000000000000000000000000000062408200000000000000000000000000
# 061:000000000000000000000000409090909090905050564646464646269090909090909090564626404040404040a940000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004040303020309040b3000000000000e2b3b340404000000009194040400000000000004040404030303000000000000000000000000064646464000000000000000000000000000000000000000000000040a94040b2e1000000000000000000646492404040404082000000000000000000000000000000000000000000000000000000000000000000000000
# 062:00000000000000404040404040409090909050505050505050505050505090909090909040404040404040404040404000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000040a9302020303040b3b3e2000000b3b3b3b3404040000000000040404000000000004040404030303030a3000000000000000000000000000000000000000000000000000000000000000000000000000040404040646400000000000000000000000040a940408200000000000000000000000000000000000000000000000000000000000023334300000000
# 063:000000000000404090909040409030b73090909090905050374750909090303030303090909040303090233343909090a9000000000000000000000000000000000000000000000000000040000000000000000000004040000000000000000000091940a9302020203040e3b3b3b3b3b3b3b3b3e34040400000000000404040000000004040a9403030303030a40000000000000000000000000000000000006464646464646464000000000000000000000000404040b20000000000000000000000000000624040820000000000000000000000000000000000000000000000000000000000000024344400000000
# 064:00000000004040902333439090b73020303090909090909038489090909030302020303030909030304024344440409026464646464646464646464646464646464646464646464656404040304040304040263646564030404000000000000000000040903020202030a9e3e3b3b3e3e3e3b3b3e3403030192900000000000000000040404040403030202020000000000000006464646464000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000025354500000000
# 065:009090909090303024344490303020202030303030903030b7303030303030202010102030303030203030303090404000000000000000000000000000000000000000000000000000909030304030203040404040404020309040404040264646465640302020102030a9e3e3e3e3e3e3e3e3e3e3403030000000000000000000004040404030303020202020006464646400000000000000000000000000000000000000000000006464646464640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000374721313747000000
# 066:404040404030202030354530302020101020203030303020202020202020202010102020202020202020202030909090a300000000000000000000000000000000000000000000000090402020202020203030309090902020203030404040404040403020201010202030e3e3e3e3e3e3e3e3e3e3403020300000000000000000404040303030302020101010a300000000000000000000000064646464646464000000000000000000000000000000000000000000000000e1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000384822323848000000
# 067:403030303030202020202020202010101020202020202020101010101020101010102010101010101020202030303030a400000000000000000000000000000000000000000000009090302010101010202020303040402010103030303040404040303020201010102030e3e3e3e3e3e3e3e3e3e3302020203040404040404040404030303030202020101010a40000000000000000000000000000000000000000000000000000000000000000000000646464404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040
# </MAP>

# <WAVES>
# 000:00000000ffffffff00000000ffffffff
# 001:0123456789abcdeffedcba9876543210
# 002:0123456789abcdef0123456789abcdef
# </WAVES>

# <SFX>
# 000:000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000104000000000
# </SFX>

# <TRACKS>
# 000:100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# </TRACKS>

# <FLAGS>
# 000:0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# </FLAGS>

# <PALETTE>
# 000:1a1c2c5d275db13e53ef7d57ffcd75a7f07038b76425717929366f3b5dc941a6f673eff7f4f4f494b0c2566c86333c57
# </PALETTE>

