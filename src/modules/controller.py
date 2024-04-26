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
    width=16
    height=16
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

    def PlayerKontroler(self, coll):
        self.coll=coll
        #skakanje
        if key(48) and not self.jumped: #and self.vsp == 0: #<- ovo je manje bugged ali bez coyote time
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
            self.vsp=0
            while self.y<self.minY and not self.ProvjeriKolizije(self, 0, 1):
                self.y+=1
        else:
            self.vsp=self.vsp+self.gravitacija

        if self.vsp<0:
            if self.ProvjeriKolizije(self, 0, self.vsp - 1):
                self.vsp=0

        

        #blokiranje lijevo i desno
        if self.x>(pogled.ogranicenjeX - self.width) or self.ProvjeriKolizije(self, 1+self.hsp, 0):
            self.hsp=0
            while self.ProvjeriKolizije(self, 0, 0) or self.x > (pogled.ogranicenjeX - self.width):
                self.x-=1
            
        if self.x<0 or self.ProvjeriKolizije(self, -1+self.hsp, 0):
            self.hsp=0
            while self.ProvjeriKolizije(self, 0, 0) or self.x < 0:
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

            
            
    def JetpackJoyride(self):
        if self.jetpackGorivo > 0:
            self.vsp = -self.jetpackJacina
            self.jetpackGorivo = self.jetpackGorivo - 1
            self.skok = 0
     
    


