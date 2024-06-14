def pomakni(a, b, vrijednost):
    if vrijednost == 0:
        return a
    elif a < b:
        return min(a + vrijednost, b)
    else:
        return max(a - vrijednost, b)

ladder_tile_indexes = [
    48, 49, 64, 65, 80, 81, 96, 97
]

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
    skok=0
    coll=[]
    spriteTimer = 0
    on_ladders = False

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
    acc_normal = 0.25
    acc_ladders = 1
    akceleracija = 0.25
    maxBrzina=2
    gravitacija=0.24


    #Varijable skakanja
    skokJacina=4.4
    
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
        self.CheckOnLadders(self)

        #promjena akceleracije ovisno o ljestvama
        if self.on_ladders:
            self.akceleracija = self.acc_ladders
        else:
            self.akceleracija = self.acc_normal

        #skakanje
        if key_space and self.vsp == 0: #<- ovo je manje bugged ali bez coyote time  #and not self.jumped:
            if self.ProvjeriKolizije(self, 0, 1) or self.y>=self.minY or self.ctVar < self.coyoteTime or self.on_ladders:
                self.vsp = -self.skokJacina
                self.jumped = True
                self.on_ladders = False

        #coyote time
        if not self.on_ladders:
            if self.ProvjeriKolizije(self, 0, 1):
                self.ctVar = 0
                self.jumped = False
            else:
                self.ctVar += 1
        

        #kretanje lijevo desno
        if key_left: 
            self.hsp=pomakni(self.hsp,-self.maxBrzina,self.akceleracija)
            self.desno=False
            self.is_walking = True
        elif key_right:
            self.hsp=pomakni(self.hsp,self.maxBrzina,self.akceleracija)
            self.is_walking = True
            self.desno=True
        else:
            self.hsp=pomakni(self.hsp,0,self.akceleracija)
            self.is_walking = False
            

        #gravitacija i kolizije
        if self.y+self.vsp>=self.minY or self.ProvjeriKolizije(self, 0, self.vsp + 1):
            if self.vsp > 0:
                while self.y<self.minY and not self.ProvjeriKolizije(self, 0, 1):
                    self.y+=1
            self.vsp=0
        else:
            if not self.on_ladders:
                self.vsp=self.vsp+self.gravitacija
                if self.ProvjeriKolizije(self, 0, self.vsp):
                    self.vsp = 0

        if self.vsp<0:
            if self.ProvjeriKolizije(self, 0, self.vsp - 1):
                self.vsp=0

        #pomicanje po ljestvama
        if self.on_ladders:
            if key_up: 
                self.vsp=pomakni(self.vsp,-self.maxBrzina,self.akceleracija)
            elif key_down:
                self.vsp=pomakni(self.vsp,self.maxBrzina,self.akceleracija)
            else:
                self.vsp=pomakni(self.vsp,0,self.akceleracija)
            
            if self.ProvjeriKolizije(self, 0, self.vsp) or self.y + self.vsp >= self.minY:
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

        if self.is_walking == True:
            self.spriteTimer += 0.1
        elif self.on_ladders:
            if key_up or key_down:
                self.spriteTimer += 0.1

        #renderanje spritea
        if self.on_ladders:
            spr(290 + 2*(round(self.spriteTimer)%2==0),int(self.x) - int(pogled.x),int(self.y) - int(pogled.y),6,1,0,0,2,2)
        else:
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

        self.UnStuck(self)
     
    def Pogoden(self, dmg):
        global state
        self.health -= dmg
        self.hitVar = 0
        if self.health < 1:
            state = 'over'

    def CheckOnLadders(self):
        if self.on_ladders:
            for i in range(0, int(self.width), int(self.width/2)):
                for j in range(0, int(self.height), int(self.height/2)):
                    if mget(round((self.x + i)/8), round((self.y + j)/8) + level*LEVEL_HEIGHT) in ladder_tile_indexes:
                        return
            self.on_ladders = False
        else:
            if not key_up and not key_down:
                return
            for i in range(0, int(self.width), int(self.width/2)):
                for j in range(0, int(self.height), int(self.height/2)):
                    if mget(round((self.x + i)/8), round((self.y + j)/8) + level*LEVEL_HEIGHT) in ladder_tile_indexes:
                        self.on_ladders = True

    def UnStuck(self):
        if self.ProvjeriKolizije(self, 0, 0):
            for skok in range (1, 3):
                for i in range (-skok, skok, skok):
                    for j in range (-skok, skok, skok):
                        if i == 0 and j == 0:
                            continue
                        if not self.ProvjeriKolizije(self, i, j):
                            self.x += i
                            self.y += j
                            return