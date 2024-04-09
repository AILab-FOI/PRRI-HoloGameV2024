# title:   HoloGameV
# author:  AILab-FOI
# desc:    short description
# site:    https://ai.foi.hr
# license: GPLv3
# version: 0.1
# script:  python

t=0
x=96
y=24

def TIC():
 PlayerKontroler()


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
def test( a, b ):
    return a+b
# <TILES>
# 001:eccccccccc888888caaaaaaaca888888cacccccccacc0ccccacc0ccccacc0ccc
# 002:ccccceee8888cceeaaaa0cee888a0ceeccca0ccc0cca0c0c0cca0c0c0cca0c0c
# 003:eccccccccc888888caaaaaaaca888888cacccccccacccccccacc0ccccacc0ccc
# 004:ccccceee8888cceeaaaa0cee888a0ceeccca0cccccca0c0c0cca0c0c0cca0c0c
# 017:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 018:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
# 019:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 020:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
# </TILES>

# <WAVES>
# 000:00000000ffffffff00000000ffffffff
# 001:0123456789abcdeffedcba9876543210
# 002:0123456789abcdef0123456789abcdef
# </WAVES>

# <SFX>
# 000:000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000304000000000
# </SFX>

# <TRACKS>
# 000:100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# </TRACKS>

# <PALETTE>
# 000:1a1c2c5d275db13e53ef7d57ffcd75a7f07038b76425717929366f3b5dc941a6f673eff7f4f4f494b0c2566c86333c57
# </PALETTE>

