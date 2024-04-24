# title:   game title
# author:  game developers, email, etc.
# desc:    short description
# site:    website link
# license: MIT License (change this to your license of choice)
# version: 0.1
# script:  python

id=0

def SoundEffects():
 global id

 if key(1): sfx(2, "C-4")
 if key(19): sfx(4, "C-4")
 if key(4): sfx(11, "C-4")
 if key(6): sfx(1, "C-4")
 if key(7): sfx(3, "C-4")
 if key(8): sfx(7, "C-4")
 if key(10): sfx(5, "C-4")
 if key(11): sfx(6, "C-4")
 if key(12): sfx(8, "C-4")
 if key(13): sfx(9, "C-4")
 if key(14): sfx(10, "C-4")
 
 cls(13)
 print("Stisnite 'A' za efekt prvog blastera.",10,10)
 print("Stisnite 'S' za efekt drugog  blastera.",10,20)
 print("Stisnite 'D' za efekt treceg  blastera.",10,30)
 print("Stisnite 'F' za efekt prvog neprijatelja.",10,40) 
 print("Stisnite 'G' za efekt drugog neprijatelja.",10,50) 
 print("Stisnite 'H' za efekt treceg  neprijatelja.",10,60) 
 print("Stisnite 'J' za efekt bossovih koraka.",10,70) 
 print("Stisnite 'K' za efekt kliznih vrata.",10,80) 
 print("Stisnite 'L' za efekt smrt igraca.",10,90) 
 print("Stisnite 'N' za efekt skoka igraca.",10,100)
 print("Stisnite 'M' za efekt uzimanja oruzja.",10,110) 
  
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
# 001:0497047504540442144214411441145414502450246f346f347f448f448f448f548e548e548e648e648d748d749d849d849d94ada4cdc4dce4fcf4fc112000000000
# 002:5596859695d5a5b4b593c592c59fd59ed58de58de57ce56cf55cf53bf53bf52af51af519f518f518f508f508f508f508f508f508f508f508f508f508300000000400
# 003:0ef01ec02eb03ea04e905e806e707e608e409e30ae30be20ce20de10de10ee10fe00fe00fe00fe00fe00fe00fe00fe00fe00fe00fe00fe00fe00fe00304000000500
# 004:11f721d631c441a35191518f617c716981589150a140a140b130c130d120e120f120f120f120f120f120f120f120f120f120f120f120f120f120f120307000000009
# 005:451065008500a500b500c500d500d500d500e500e500f500f500f500f500f500f500f500f500f500f500f500f500f500f500f500f500f500f500f5003f2000000100
# 006:c6077604060416013600460f560e760d860ca60bb60ac609c609d600d600d600e600e600e600f600f600f600f600f600f600f600f600f600f600f600b6000000000d
# 007:07168730076d1777470e8708e700f700f700f700f700f700f700f700f700f700f700f700f700f700f700f700f700f700f700f700f700f700f700f700370000000406
# 008:3748873837188748476897485708a70867099709470a970b670b970c770db70e670fb70f8701d7029703d703c704d705d706d706d707d707e707f700360000000000
# 009:e700970f670ed70df700e70dc70ca70b570cf700f700f700f700f700f700f700f700f700f700f700f700f700f700f700f700f700f700f700f700f700b60000000000
# 010:3708570837f157ffa7f7c7f7d7f7d7f7e7f7e7f7f7f7770887089708b708c708c708e708e708e708e708e708f708f708f708f708f708f708f708f708900000000000
# 011:0307031603250334034303520361037f038e239d43ac63bb83caa3d9c3e8f3f8f3f8f3f8f3f8f3f8f3f8f3f8f3f8f3f8f3f8f3f8f3f8f3f8f3f8f3f8d80000000000
# </SFX>

# <TRACKS>
# 000:100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# </TRACKS>

# <PALETTE>
# 000:1a1c2c5d275db13e53ef7d57ffcd75a7f07038b76425717929366f3b5dc941a6f673eff7f4f4f494b0c2566c86333c57
# </PALETTE>

