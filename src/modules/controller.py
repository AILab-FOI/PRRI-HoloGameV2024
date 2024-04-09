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