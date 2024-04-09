



class player: 
    x=96
    y=24
    desno=False
    shootTimer=0
    jetpackGorivo=0
    skok=0 
    


minY=120 #najniza tocka
minX=225 #najdesnija tocka

#Osnovne Varijable
brzina=3
gravitacija=2

#Varijable skakanja
skokTrajanje=20
skokJacina=2

#jetpack
jetpackTrajanje=50
jetpackJacina=4




def PlayerKontroler():
    global skokTrajanje, skokJacina, minY, minX, brzina, gravitacija


     #skakanje
    if btn(0):
	    if player.y==minY:
		    player.skok=skokTrajanje 
                
    if key(48):
        if player.y==minY:
            player.skok=skokTrajanje 
    
    if player.skok>0:
        player.y=player.y-skokJacina
        player.skok=player.skok-1 


    #kretanje lijevo desno
    if key(1): 
        player.x=player.x-brzina
        player.desno=False
    if key(4):
        player.x=player.x+brzina
        player.desno=True

    if key(23):
        JetpackJoyride()
        

    #gravitacija
	if player.y<minY:
		if player.skok<1:
		    player.y=player.y+gravitacija
	else: 
		player.y=minY


	#blokiranje lijevo i desno
	if player.x>minX:
		player.x=minX
		
    if player.x<0:
        player.x=0
        
    
    #jetpack
    
    if player.y == minY:
        player.jetpackGorivo=jetpackTrajanje
    
        
    #renderanje spritea
    if player.desno==True:
        spr(1+t%60//30*2,player.x,player.y,14,1,1,0,2,2)
    else:
        spr(1+t%60//30*2,player.x,player.y,14,1,0,0,2,2)
        
        
def JetpackJoyride():
    if player.jetpackGorivo > 0:
        player.y = player.y - jetpackJacina
        player.jetpackGorivo = player.jetpackGorivo - 1
        player.skok = 0
     
        


