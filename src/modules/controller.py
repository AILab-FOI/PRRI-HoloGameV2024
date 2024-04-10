



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
     
        


