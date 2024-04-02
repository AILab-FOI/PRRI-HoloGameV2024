-- title:   Hologame-V
-- author:  Leonardo Andrasic
-- desc:    Igra za PRRI
-- site:    website link
-- license: MIT License (change this to your license of choice)
-- version: 0.1
-- script:  python 


t=0
x=96
y=24


minY=120 --najniza tocka
minX=225 --najdesnija tocka


--Osnovne Varijable
brzina=3
gravitacija=2


--Varijable skakanja
skokVar=0 
skokTrajanje=20
skokJacina=2


function TIC()

 --skakanje
 if btn(0) then if y==minY then 
	skokVar=skokTrajanje 
	end print() end
	
	if key(48) then if y==minY then 
	skokVar=skokTrajanje 
	end print() end
	
	if skokVar>0 then
	y=y-skokJacina
	skokVar=skokVar-1 
	end
	
	
	--kretanje lijevo desno
	if btn(2) then x=x-brzina end
	if btn(3) then x=x+brzina end
	
	
 -- gravitacija
	if y<minY then if skokVar<1
	 then y=y+gravitacija end
	else y=minY end

	
	--blokiranje lijevo i desno
	if x>minX then x=minX end
 if x<0 then x=0 end
	
	
	--nez
	cls(13)
	spr(1+t%60//30*2,x,y,14,1,0,0,2,2)
	t=t+1
	
end

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

