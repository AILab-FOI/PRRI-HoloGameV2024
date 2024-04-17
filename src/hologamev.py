# title:   HoloGameV
# author:  AILab-FOI
# desc:    short description
# site:    https://ai.foi.hr
# license: GPLv3
# version: 0.1
# script:  python

t=0

def TIC():
 Final()
 Pucanje()
 collidables = DefinirajKolizije()
 PlayerKontroler(collidables)
 




def Final():
	cls(13)
    print("A i D za kretanje, SPACE za skakanje", 0, 0)
    print("W za jetpack, F i G za pucanje", 0, 8)
 
	t=t+1


class collidable:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.draw_self()

    def check_collision(self, other):
        if self.x < other.x + other.width and self.x + self.width > other.x and self.y < other.y + other.height and self.y + self.height > other.y:
            return True
        return False

    def check_collision_rectangle(self, xleft, ytop, xright, ybottom):
        if self.x < xright and self.x + self.width > xleft and self.y < ybottom and self.y + self.height > ytop:
            return True
        return False

    def draw_self(self):
        rect(self.x, self.y, self.width, self.height, 15)


def DefinirajKolizije():
    coll1 = collidable(20, 70, 60, 15)
    coll2 = collidable(200, 112, 40, 10)
    coll3 = collidable(150, 80, 30, 10)
    collidables = [coll1, coll2, coll3]
    return collidables




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
        player.is_walking = True
    elif key(4):
        player.hsp=pomakni(player.hsp,maxBrzina,akceleracija)
        player.is_walking = True
        player.desno=True
    else:
        player.hsp=pomakni(player.hsp,0,akceleracija)
        player.is_walking = False

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

    if player.is_walking == True:
        player.spriteTimer += 0.1

    print(player.spriteTimer, 0, 32)

    #renderanje spritea
    if player.desno==True and player.is_walking==True:
        spr(258 + 2*(round(player.spriteTimer)%2==0),int(player.x),int(player.y),14,1,0,0,2,2)
    elif player.desno==False and player.is_walking==True:
        spr(258 + 2*(round(player.spriteTimer)%2==0),int(player.x),int(player.y),14,1,1,0,2,2)
    else:
        spr(player.frame,int(player.x),int(player.y),14,1,0,0,2,2)

        
        
def JetpackJoyride():
    if player.jetpackGorivo > 0:
        player.vsp = -jetpackJacina
        player.jetpackGorivo = player.jetpackGorivo - 1
        player.skok = 0
     
        






class prvaPuska:
    x=0
    y=0
    
    desno=False
    
    firerate = 0.6
    speed=16
    dmg=4
    
class drugaPuska:
    x=0
    y=0
    
    desno=False
    
    firerate = 0.1
    speed=6
    dmg=1


metci = []



   

def Pucanje():
    
    player.shootTimer = player.shootTimer - 1
    
    if player.shootTimer < 0:
        if key(6):
            pucaj(prvaPuska)
        if key(7):
            pucaj(drugaPuska)
        
    for metak in metci:
            spr(1,metak.x,metak.y,14,1,0,1,1,1)
            
            if metak.desno == True:   
                metak.x = metak.x + metak.speed
            else:
                metak.x = metak.x - metak.speed
            
            if metak.x < 0 or metak.x > minX:
                del metak

def pucaj(puska):
  metak = puska()  
  metak.x = int(player.x)
  metak.y = int(player.y)
  metak.desno = player.desno

  metci.append(metak)
  player.shootTimer=puska.firerate*60
  




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

# <SPRITES>
# 000:000000fe00000fee0000feee0000feee00000fee000000fe00000e0000fee034
# 001:d0000000ed00000022d00000eed00000ed000000e00000000e00000040ed0000
# 002:000000fe00000fee0000feee0000ffee00000ffe000000ff00000e0000fee034
# 003:d0000000ed00000022d00000eed00000ed000000e00000000e00000040eed000
# 004:000000fe00000fee0000feee0000ffee00000ffe000000ff00000ee000000e03
# 005:d0000000ed00000022d00000eed00000ed000000e00000000e00000040000000
# 006:000000fe00000fee0000feee0000ffee00000ffe000000ff00000ee000000e03
# 007:d0000000ed00000022d00000eed00000ed000000e00000000f00000030fefeff
# 008:0000000d000000de00000d2200000dee000000de0000000e000000e00000de04
# 009:ef000000eef00000eeef0000eeef0000eef00000ef00000000e00000430eef00
# 010:0000000d000000de00000d2200000dee000000de0000000e000000e0000dee04
# 011:ef000000eef00000eeef0000eeff0000eff00000ff00000000e00000430eef00
# 012:0000000d000000de00000d2200000dee000000de0000000e000000e000000004
# 013:ef000000eef00000eeef0000eeff0000eff00000ff0000000ee0000030e00000
# 016:00feee0300feffe000fe0fe000fe0eee000ffee00000fe000000fe000000fff0
# 017:0eeed000ef0ee000ee0ee000ed00e000fed00000fee00000fee000000fee0000
# 018:0feeee030fe0f0e00fee0fe000f00eee0000fee00000fe00000fee00000ffee0
# 019:0ee0ed00e0e0ee00ee00eed0ed000d00fed00000ffed00000ffd000000fed000
# 020:0000eee00000eeee0000efee00000ffe00000fee0000fee00000fe0000000ff0
# 021:0e000000e0000000ee000000ed000000fe000000ffe00000fee00000ff000000
# 022:0000eee00000eeee0000efee00000ffe00000fee0000fee00000fe0000000ff0
# 023:0effeff0eff0f000ee00f000ed000000fe000000ffe00000fee00000ff000000
# 024:000deee0000ee0fe000ee0ee000e00de00000def00000eef00000eef0000eef0
# 025:30eeef000effef000ef0ef00eee0ef000eeff00000ef000000ef00000fff0000
# 026:00de0ee000ee0e0e0dee00ee00d000de00000def0000deff0000dff0000def00
# 027:30eeeef00e0f0ef00ef0eef0eee00f000eef000000ef000000eef0000eeff000
# 028:000000e00000000e000000ee000000de000000ef00000eff00000eef000000ff
# 029:0eee0000eeee0000eefe0000eff00000eef000000eef000000ef00000ff00000
# 032:0000000d000000de00000d2200000dee000000de0000000e000000f0ffefef03
# 033:ef000000eef00000eeef0000eeff0000eff00000ff0000000ee0000030e00000
# 034:0000ff00000feef000ffffee0feeffff0feef00000feeff7000feef700ffff7f
# 035:0000000000000000ef00000000000000000000007dd00000fffd0000222f0000
# 036:0000ff00000feef000ffffee0feeffff0feef00000feeff7000feef700ffff7f
# 037:0000000000000000ef00000000000000000000007dd00000fffd0000233f0000
# 038:0000ff00000feef000feffee0fefffff0feef00000feefff000feef700ffff7f
# 039:0000000000000000ef000000000000000000000077d00000fffd0000233f0000
# 040:0000000000000000000000fe000000000000000000000dd70000dfff0000f222
# 041:00ff00000feef000eeffff00ffffeef0000feef07ffeef007feef000f7ffff00
# 042:0000000000000000000000fe000000000000000000000dd70000dfff0000f332
# 043:00ff00000feef000eeffff00ffffeef0000feef07ffeef007feef000f7ffff00
# 044:0000000000000000000000fe000000000000000000000d770000dfff0000f332
# 045:00ff00000feef000eeffef00fffffef0000feef0fffeef007feef000f7ffff00
# 048:0ffeffe0000f0ffe000f00ee000000de000000ef00000eff00000eef000000ff
# 049:0eee0000eeee0000eefe0000eff00000eef000000eef000000ef00000ff00000
# 050:00fee777000fe77700fee77700fe777f00fe777000fe77d0000fe77d000ffff7
# 051:f2fd00007f7d00007777000077770000f7770000fe7d00000fe7d0000ffedd00
# 052:00fee777000fe77700fee77700fe777700fe77770ffe77770fffeeee0ffffffe
# 053:f2fd00007f7d00007777000077770000700000007d00000077d00000e7700000
# 054:00fee777000fe777000fe777000fe77e00ffe77e00ffe7770feffeee0feefffe
# 055:f2f700007f770000777d000077d00000ed0000007edd0000777d0000ee770000
# 056:0000df2f0000d7f700007777000077770000777f0000d7ef000d7ef000ddeff0
# 057:777eef00777ef000777eef00f777ef000777ef000d77ef00d77ef0007ffff000
# 058:0000df2f0000d7f7000077770000777700000007000000d700000d770000077e
# 059:777eef00777ef000777eef007777ef007777ef007777eff0eeeefff0effffff0
# 060:00007f2f000077f70000d77700000d77000000de0000dde70000d777000077ee
# 061:777eef00777ef000777ef000e77ef000e77eff00777eff00eeeffef0efffeef0
# 064:a0000888aaa08999a9989999a99999ff0a999fdd00a9fddd0099fd220099fd22
# 065:880000f09980fff0999888f0f99988f0df998f00ddf980002df9f0002df9f000
# 066:a0000a99aaa0a999aa9a9999aa9999ff0aa99fdd00a9fddd0099f2220099f222
# 067:880000f09980fff0999888f0f99998f0df998f00ddf98000ddf9f000ddf9f000
# 068:a0000a99aaa0a999aa9a9999aa9999ff0aa99fdd00a9fddd0099f2220099f222
# 069:880000f09980fff0999888f0f99998f0df998f00ddf98000ddf9f000ddf9f000
# 070:0f0000880fff08990f8889990f88999f00f899fd00089fdd000f9fd2000f9fd2
# 071:8880000a99980aaa9999899aff99999addf999a0dddf9a0022df990022df9900
# 072:0f0000880fff08990f8889990f89999f00f899fd00089fdd000f9fdd000f9fdd
# 073:99a0000a999a0aaa9999a9aaff9999aaddf99aa0dddf9a00222f9900222f9900
# 074:0f0000880fff08990f8889990f89999f00f899fd00089fdd000f9fdd000f9fdd
# 075:99a0000a999a0aaa9999a9aaff9999aaddf99aa0dddf9a00222f9900222f9900
# 080:00a99fd200a999ff0a9a9999a9999888a9999980999999809999998009988800
# 081:df99f000f998f00099898f00889998f0899998f0899999f0899999f00888ff00
# 082:00a99f2d00a999ff0aaa9999aa999999a9999990999999800999880000000000
# 083:df99f000f999f00099998f00899998f0899998f0899999f0899999f00888ff00
# 084:00a99f2d00a999ff0aaa9999aa999999a9999980a99999809999998009998800
# 085:df99f000f999f00099998f00899998f0899999f0899999f00888ff0000000000
# 086:000f99fd000f899f00f898990f8999880f8999980f9999980f99999800ff8880
# 087:2df99a00ff999a009999a9a08889999a0899999a089999990899999900888990
# 088:000f99fd000f999f00f899990f8999980f8999980f9999980f99999800ff8880
# 089:d2f99a00ff999a009999aaa0999999aa0999999a089999990088999000000000
# 090:000f99fd000f999f00f899990f8999980f9999980f99999800ff888000000000
# 091:d2f99a00ff999a009999aaa0999999aa0899999a0899999a0899999900889990
# </SPRITES>

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

