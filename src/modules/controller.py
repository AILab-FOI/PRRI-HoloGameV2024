



class player: 
    x=96
    y=24
    width=16
    height=16
    hsp=0
    vsp=0
    desno=False
    shootTimer=0
    jetpackGorivo=0
    skok=0
    coll=[]

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
minX=225 #najdesnija tocka

#Osnovne Varijable
akceleracija=0.5
maxBrzina=3
gravitacija=0.3

#Varijable skakanja
skokJacina=5.2

#jetpack
jetpackTrajanje=50
jetpackJacina=2


def pomakni(a, b, vrijednost):
    if vrijednost == 0:
        return a
    elif a < b:
        return min(a + vrijednost, b)
    else:
        return max(a - vrijednost, b)



def PlayerKontroler(coll):
    player.coll=coll

     #skakanje
    if key(48) and player.vsp==0:
        if player.ProvjeriKolizije(player, 0, 1) or player.y>=minY:
            player.vsp=-skokJacina

    #letenje jetpack
    if key(24):
        JetpackJoyride()


    #kretanje lijevo desno
    if key(1): 
        player.hsp=pomakni(player.hsp,-maxBrzina,akceleracija)
        player.desno=False
    elif key(4):
        player.hsp=pomakni(player.hsp,maxBrzina,akceleracija)
        player.desno=True
    else:
        player.hsp=pomakni(player.hsp,0,akceleracija)

    if key(23):
        JetpackJoyride()
        

    #gravitacija i kolizije
    if player.y+player.vsp>=minY or player.ProvjeriKolizije(player, 0, player.vsp + 1):
        player.vsp=0
        while player.y<minY and not player.ProvjeriKolizije(player, 0, 1):
            player.y+=1
    else:
        player.vsp=player.vsp+gravitacija

    if player.vsp<0:
        if player.ProvjeriKolizije(player, 0, player.vsp - 1):
            player.vsp=0

    

	#blokiranje lijevo i desno
	if player.x>minX or player.ProvjeriKolizije(player, 1+player.hsp, 0): # ZAMIJENITI SA COLLISION PROVJEROM
        player.hsp=0
        while player.ProvjeriKolizije(player, 0, 0) or player.x > minX:
            player.x-=1
		
    if player.x<0 or player.ProvjeriKolizije(player, -1+player.hsp, 0): # ZAMIJENITI SA COLLISION PROVJEROM
        player.hsp=0
        while player.ProvjeriKolizije(player, 0, 0) or player.x < 0:
            player.x+=1

    player.x=player.x+player.hsp
    player.y=player.y+player.vsp
        
    
    #jetpack
    
    if player.ProvjeriKolizije(player, 0, 1) or player.y>=minY: # ZAMIJENITI SA DOK STOJI NA NEKOM OBJEKTU
        player.jetpackGorivo=jetpackTrajanje
    
        
    #renderanje spritea
    if player.desno==True:
        spr(1+t%60//30*2,int(player.x),int(player.y),14,1,1,0,2,2)
    else:
        spr(1+t%60//30*2,int(player.x),int(player.y),14,1,0,0,2,2)
        
        
def JetpackJoyride():
    if player.jetpackGorivo > 0:
        player.vsp = -jetpackJacina
        player.jetpackGorivo = player.jetpackGorivo - 1
        player.skok = 0
     
        


