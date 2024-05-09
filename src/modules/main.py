# title:   HoloGameV
# author:  AILab-FOI
# desc:    short description
# site:    https://ai.foi.hr
# license: GPLv3
# version: 0.1
# script:  python


state='menu' #varijabla za game state

level = 0 #koji level je ucitan
LEVEL_HEIGHT = 17

def ZapocniLevel(level):
  player.ProvjeriKolizije(player, 0, 0)


def TIC():
 Final()

 global state
 if state=='game':
   cls(0)

   map(0, level*LEVEL_HEIGHT, 36, 18, -int(pogled.x), -int(pogled.y), 0)

   collidables = DefinirajKolizije([player, enemy, metci, projectiles], level, LEVEL_HEIGHT)
   #enemy.movement(enemy, collidables)
   for projektil in projectiles:
      projektil.movement()
      Projectile.MetakCheck(projektil, collidables)
   Puska.Pucanje()
   player.PlayerKontroler(player, collidables)
   pogled.pratiIgraca()
   for metak in metci:
     Metak.MetakCheck(metak, collidables)
   for metak in projectiles:
     Projectile.MetakCheck(metak, collidables)
   PromjenaPuska.PickUp(PromjenaPuska)
 elif state=='menu':
   menu.Menu()

def Final():
	cls(13) 
  
  
  #print("A i D za kretanje, SPACE za skakanje", 0, 0)
  #print("W za jetpack, F ", 0, 8)
  #print("S za promjenu oruzja,", 0, 16)
 
	

# <TILES>
# 001:8888888888888888888888888888888888888888888888888888888888888888
# 002:9999999999999999999999999999999999999999999999999999999999999999
# 003:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
# 004:eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
# 005:dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
# 006:00dddddd0deeeeeedeeeeeeedeeeeeeedeeeeeeedeeeeeee0deeeeee00dfffff
# 007:ddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffff
# 008:dddddf00eeeeeef0eeeeeeefeeeeeeefeeeeeeefeeeeeeefeeeeeef0ffffff00
# 009:dddddddfdeeeeeefdeeeeeefdeeeeeefdeeeeeefdeeeeeefdeeeeeefdfffffff
# 010:dddddddfdeeeeeefdedeefefdeeeeeefdeeeeeefdedeefefdeeeeeefdfffffff
# 011:dddddddddd9eafa8d9eafad8deafad98dafad9e8dfad9ea8dad9eaf8d8888888
# 012:00dddddd0deeeeeedeedeeeedeeeeeeedeeeeeeedeedeeee0deeeeee00dfffff
# 013:ddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffff
# 014:dddddf00eeeeeef0eeeefeefeeeeeeefeeeeeeefeeeefeefeeeeeef0ffffff00
# 016:dddddddddeeeeeeededdeeeededdeeeedeeeeeeedeeeeeeedeeeeeeedeeeeeee
# 017:ddddddddeeeeeeefeeeeffefeeeeffefeeeeeeefeeeeeeefeeeeeeefeeeeeeef
# 018:ffffffffffeeeeeefefeeeeefeefeeeefeeefeeefeeeeffffeeeeff2feeeef2f
# 019:ffffffffeeeeeeffeeeeefefeeeefeefeeefeeeffffeeeef2ffeeeeff2feeeef
# 020:000ddddd00deeeef0deeeeefdeeeeeefdeeeeeefdeeeeeefdeeeeeefdfffffff
# 021:ddddf000feeeef00feeeeef0feeeeeeffeeeeeeffeeeeeeffeeeeeefffffffff
# 022:000ddddd00deeeee0deeeeeedeeeeeeedeeeeeeedeeeeeeedeeeeeeedeeeeeee
# 023:ddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
# 024:ddddf000eeeeef00eeeeeef0eeeeeeefeeeeeeefeeeeeeefeeeeeeefeeeeeeef
# 025:000ddddd00deeeee0deeddeedeeeddeedeeeeeeedeeeeeeedeeeeeeedeeeeeee
# 026:ddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
# 027:ddddf000eeeeef00eeffeef0eeffeeefeeeeeeefeeeeeeefeeeeeeefeeeeeeef
# 028:3333333333444444343444443443444434443444344443443444443434444443
# 029:3333333344444433444443434444344344434443443444434344444334444443
# 030:8888888888bbbb888b8bb8b88bb88bb88bb88bb88b8bb8b888bbbb8888888888
# 032:deeeeeeedeeeeeeedeeeeeeedeeeeeeededdeeeededdeeeedeeeeeeeffffffff
# 033:eeeeeeefeeeeeeefeeeeeeefeeeeeeefeeeeffefeeeeffefeeeeeeefffffffff
# 034:feeeef2ffeeeeff2feeeeffffeeefeeefeefeeeefefeeeeeffeeeeeeffffffff
# 035:f2feeeef2ffeeeeffffeeeefeeefeeefeeeefeefeeeeefefeeeeeeffffffffff
# 036:dfffffffdeeeeeefdeeeeeefdeeeeeefdeeeeeef0deeeeef00deeeef000fffff
# 037:fffffffffeeeeeeffeeeeeeffeeeeeeffeeeeeeffeeeeef0feeeef00fffff000
# 038:deeeeeeedeeeeeeedeeeeeeedeeeeeeedeeeeeee0deeeeee00deeeee000fffff
# 039:eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffff
# 040:eeeeeeefeeeeeeefeeeeeeefeeeeeeefeeeeeeefeeeeeef0eeeeef00fffff000
# 041:deeeeeeedeeeeeeedeeeeeeedeeeddeedeeeddee0deeeeee00deeeee000fffff
# 042:eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffff
# 043:eeeeeeefeeeeeeefeeeeeeefeeffeeefeeffeeefeeeeeef0eeeeef00fffff000
# 044:3444444334444434344443443444344434434444343444443344444433333333
# 045:3444444343444443443444434443444344443443444443434444443333333333
# 046:3333333333444433343443433443344334433443343443433344443333333333
# 048:dddddddddd000000dddddddddd000000dddddddedd000000dddddeeedd000000
# 049:dddeeeee000000eedeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000ee
# 050:dddddddddeeeeeeedeeeeeeedeeeeeeedeeeffffffefddedffefdedddeefedde
# 051:ddddddddeeeeeeeeeeeeeeeeeeeeeeeeffffffffdeeddddeeeddddededdddedd
# 052:dddddddfeeeeeeefeeeeeeefeeeeeeefffffeeefddddfeffdddefeffddeefeef
# 053:00aaaaaa0aaaaaaaa8888888a8aa8aa8a8aa8aa8a88888880a88888800aaaaaa
# 054:aaaaaaaaaaaaaaaa88888888aa8aa8aaaa8aa8aa8888888888888888aaaaaaaa
# 055:aaaaaa00aaaaaaa08888888a8aa8aa8a8aa8aa8a8888888a888888a0aaaaaa00
# 056:0000000800000084000008440000844400084444008444480888888084884800
# 057:8888800083384800833844808888444880084448000088880000088800000008
# 058:000000000000000000000000800000008000000088888800eeeee880e8888e88
# 059:2222222222222222222222222222222222222222222222222222222222222222
# 060:3333333333333333333333333333333333333333333333333333333333333333
# 061:4444444444444444444444444444444444444444444444444444444444444444
# 062:1111111111111111111111111111111111111111111111111111111111111111
# 064:dddeeeeedd000000ddeeeeeede000000deeeeeeede000000deeeeeeede000000
# 065:eeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000ee
# 066:deefddeedeefdeeddeeeffffdeeeeeeedeeeeeeedeeddddddeedeeeedeedeeee
# 067:ddddeddddddeddddffffffffeeeeeeeeeeeeeeeeddddddddeeeeeeeeeeeeeeee
# 068:deedfeefeeddfeefffffeeefeeeeeeefeeeeeeefddddfeefeeeefeefeeeefeef
# 069:ddddddddd77777770f77777700ffffff0007f0000007f0000007f0000007f000
# 070:dddddddd7777777777777777ffffffff00000000000000000000000000000000
# 071:dddddddd7777777f777777f0ffffff000007f0000007f0000007f0000007f000
# 072:8888880084884800888888800844444800844444000844440008444400888888
# 073:0000000800000008000000080000000880000000800000008000000088000000
# 074:e80008e8e8000080e8000000ee8000008ee80000088000000000000000000000
# 075:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# 076:7777777777777777777777777777777777777777777777777777777777777777
# 077:6666666666666666666666666666666666666666666666666666666666666666
# 078:5555555555555555555555555555555555555555555555555555555555555555
# 080:eeeeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000
# 081:eeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000ee
# 082:deedeeeeffedeeeeffedeeeedeedeeeedeedffffdeeeeeeedeeeeeeedfffffff
# 083:eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffeeeeeeeeeeeeeeeeffffffff
# 084:eeeefeefeeeefeffeeeefeffeeeefeeffffffeefeeeeeeefeeeeeeefffffffff
# 085:ddddddddd33383330f33383300ffffff0003f0000003f0000003f0000003f000
# 086:dddddd8d8333383333333833ffffffff00000000000000000000000000000000
# 087:dddddddf3333333f333833f0ffffff000003f0000003f0000003f0000003f000
# 088:00888888ddeeeeefddeeeeeeddeeeeeeddeeeeeeddeeeeeeddeeeeeeddeeeeee
# 089:88000000ffff0000ffff0000ffff0000ffff0000ffff0000ffff0000ffff0000
# 091:ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
# 096:eeeeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000
# 097:eeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000eeeeeeeeee000000ee
# 098:ddf00000deef0000deeedddddeeeeeeedeeeeeeedeeeffffdeef0000dff00000
# 099:0000000000000000ddddddddeeeeeeeeeeeeeeeeffffffff0000000000000000
# 100:0000000000000000ddddddddeeeeeeeeeeeeeeeeffffffff0000000000000000
# 101:00000ddf0000deefddddeeefeeeeeeefeeeeeeefffffeeef0000deef00000dff
# 102:0000004800000848000088400004440000088000000880000084480008888880
# 103:8000000088bb000088bbb000bbbbb0000bbbb000000000000000000000000000
# 104:ddddddd8dbbbbbb8d9999998dbbbbbb8d9999998dbbbbbb8d9999998d8888888
# 112:888888888fffffff8fff22228222ff3382ff333f8f3333ff83322fff8fff2222
# 113:88888888ffffff33223333ff33ff2222fffff3fff3333fff3ffffff222f22f2f
# 114:8888888833333338fff3fff8233f33f822222228fffff33822fffff8ff2ffff8
# 115:ffffffffffeeeeeefefeeeeefeefeeeefeeefeeefeeeeffffeeeeff5feeeef5f
# 116:ffffffffeeeeeeffeeeeefefeeeefeefeeefeeeffffeeeef5ffeeeeff5feeeef
# 118:ddddddddd44444440f44444400ffffff0004f0000004f0000004f0000004f000
# 119:dddddddd4444444444444444ffffffff00000000000000000000000000000000
# 120:dddddddd4444444f444444f0ffffff000004f0000004f0000004f0000004f000
# 128:82fff3ff832333ff8ff2fff28fff222f8f33333f83fffff38fffffff88888888
# 129:ff2ff2ffffffffff2ffffff32f22233ff2ff22fffff3322f3333ff2288888888
# 130:fff22ff8fffff2f833fffff8ff33f228ffff2ff8fff2f3f8ff2fff3888888888
# 131:feeeef5ffeeeeff5feeeeffffeeefeeefeefeeeefefeeeeeffeeeeeeffffffff
# 132:f5feeeef5ffeeeeffffeeeefeeefeeefeeeefeefeeeeefefeeeeeeffffffffff
# </TILES>


# <SPRITES>
# 000:666666006666600566600055660011116605055466000544666000446600e154
# 001:0006666655006666555006661111066644040666440406664444066644440666
# 002:600066006050600560000055666011116660555466605544666000546660ee15
# 003:0006666655006666555006661111066644040666440406664444066644440666
# 004:666666006000600560500055600011116660555466605544666000546660ee15
# 005:0006666655006666555006661111066644040666440406664444066644440666
# 006:666666006000600560500055600011116660555466605544666000546660ee15
# 007:0006666655006666555006661111066644040666440406664444066644440666
# 008:666666006000600560500055600011116660555466605544666000546600ee15
# 009:0006666655006666555006661111066644040666440406664444066644440666
# 010:6666660066666002666000226600222266020222660002226660002266002222
# 011:0006666622006666222006662222066622020666220206662222066622220666
# 012:6666660060006002602000226000222266602222666022226660002266602222
# 013:0006666622006666222006662222066622020666220206662222066622220666
# 016:660eee15600ee0e160ee0eee6044000060000eee6660ee00660ee00666000066
# 017:55500666eee00666110e0666001ee066eee040660ee0066660ee066660000666
# 018:6660ee016600e0ee660440ee660000006660eee0660ee0066600006666666666
# 019:555000661ee04066e10ee066000006660eee0066600ee0666600006666666666
# 020:6660ee016600e0ee660ee0ee66044000660000ee6660ee00660eee0666000066
# 021:555000661ee04066e10ee0660011e066eee006660ee0066660ee066660000666
# 022:660eee01660ee00e660eee406660ee40666000006660eee06660ee0066600006
# 023:555066661ee06666e10e666600116666eee06666ee0066660ee0666600006666
# 024:66000e0160ee0ee060ee0eee60440ee06600eeee6660ee00660eee0666000066
# 025:5550006600004066ee0e4066eeee4066000006660ee0066660ee066660000666
# 026:6602222260022022602202226022000060000222666022006602200666000066
# 027:2220066622200666220206660022206622202066022006666022066660000666
# 028:6660220266002022660220226602200066000022666022006602220666000066
# 029:2220006622202066220220660022206622200666022006666022066660000666
# 032:6000660060206002600000226660222266602222666022226660002266602222
# 033:0006666622006666222006662222066622020666220206662222066622220666
# 034:6666666066666605666660556666011160060555044015550ee015550eeee155
# 035:0006666655006666555066661111066655550666555506665555066655550006
# 036:666666606666660566666055666601116666055566601555600015550440e155
# 037:0006666655006666555066661111066655550666555500065555044055550ee0
# 038:66666000666600556600055560011111605055446000544466000444600e1544
# 039:0066666650066666550066661110666640406666404066664440666644406666
# 040:66666000666600556600055560011111605055446000544466000444600e1544
# 041:0066666650066666550066661110666640406666404066664440666644400000
# 042:66666000666600556600055560011111605055446000544466000444600e1544
# 043:0066666650066666550066661110666640406666404066664440666644406666
# 044:666666fe66666fee6666feee6666feee66666fee666666fe66600e0066fee034
# 045:d6666666ed66666622d66666eed66666ed666666e66666660e00666640ed6666
# 048:6660220266002022660220226600000066602220660220066600006666666666
# 049:2220006622202066220220660000066602220066600220666600006666666666
# 050:600eee15660ee0e166000eee6666000066600eee6660eee0660ee00666000066
# 051:55e00440eee0eee0110eee0000110066eee0066600ee06666000066666666666
# 052:0eeeee15600ee0e1660eeeee666000006660eeee660ee0006600006666666666
# 053:55e0eee0eee0ee06110ee00600110666eee066660ee0066660ee066660000666
# 054:60eee15500ee0e1e0ee0eee1044000000000eeee660ee00060ee006660000666
# 055:55006006e000022000422400ee420066ee000666ee0066660ee0666600006666
# 056:60eee15500ee0e1e0ee0eee1044000000000eeee660ee00060ee006660000666
# 057:55003330e000030000430930ee439300ee000006ee0066660ee0666600006666
# 058:60eee15500ee0e1e0ee0eee1044000000000eeee660ee00060ee006660000666
# 059:55006006e0000aa0004aa5aaee4a5aaaee00aa00ee0000660ee0666600006666
# 060:66feee0366feffe066fe6fe066fe6eee666ffee66666fe666666fe666666fff6
# 061:0eeed666ef6ee666ee6ee666ed66e666fed66666fee66666fee666666fee6666
# 064:666666fe66666fee6666feee6666ffee66666ffe666666ff66600e0066fee034
# 065:d6666666ed66666622d66666eed66666ed666666e66666660e00666640eed666
# 066:666666fe66666fee6666feee6666ffee66666ffe666666ff66666ee066666e03
# 067:d6666666ed66666622d66666eed66666ed666666e66666660e66666640666666
# 068:666666fe66666fee6666feee6666ffee66666ffe666666ff66666ee066666e03
# 069:d6666666ed66666622d66666eed66666ed666666e66666660f66666630fefeff
# 070:6666ff66666feef666ffffee6feeffff6feef66666feeff7666feef766ffff7f
# 071:6666666666666666ef66666666666666666666667dd66666fffd6666222f6666
# 072:6666ff66666feef666ffffee6feeffff6feef66666feeff7666feef766ffff7f
# 073:6666666666666666ef66666666666666666666667dd66666fffd6666233f6666
# 074:6666ff66666feef666feffee6fefffff6feef66666feefff666feef766ffff7f
# 075:6666666666666666ef666666666666666666666677d66666fffd6666233f6666
# 076:a6666888aaa68999a9989999a99999ff6a999fdd66a9fddd6699fd226699fd22
# 077:886666f69986fff6999888f6f99988f6df998f66ddf986662df9f6662df9f666
# 080:6feeee036fe6f0e06fee6fe066f66eee6666fee66666fe66666fee66666ffee6
# 081:0ee6ed66e0e6ee66ee66eed6ed666d66fed66666ffed66666ffd666666fed666
# 082:6666eee06666eeee6666efee66666ffe66666fee6666fee66666fe6666666ff6
# 083:0e666666e0666666ee666666ed666666fe666666ffe66666fee66666ff666666
# 084:6666eee06666eeee6666efee66666ffe66666fee6666fee66666fe6666666ff6
# 085:0effeff6eff6f666ee66f666ed666666fe666666ffe66666fee66666ff666666
# 086:66fee777666fe77766fee77766fe777f66fe777666fe77d6666fe77d666ffff7
# 087:f2fd66667f7d66667777666677776666f7776666fe7d66666fe7d6666ffedd66
# 088:66fee777666fe77766fee77766fe777766fe77776ffe77776fffeeee6ffffffe
# 089:f2fd66667f7d66667777666677776666766666667d66666677d66666e7766666
# 090:66fee777666fe777666fe777666fe77e66ffe77e66ffe7776feffeee6feefffe
# 091:f2f766667f776666777d666677d66666ed6666667edd6666777d6666ee776666
# 092:66a99fd266a999ff6a9a9999a9999888a9999986999999869999998669988866
# 093:df99f666f998f66699898f66889998f6899998f6899999f6899999f66888ff66
# 096:a6666a99aaa6a999aa9a9999aa9999ff6aa99fdd66a9fddd6699f2226699f222
# 097:886666f69986fff6999888f6f99998f6df998f66ddf98666ddf9f666ddf9f666
# 098:a6666a99aaa6a999aa9a9999aa9999ff6aa99fdd66a9fddd6699f2226699f222
# 099:886666f69986fff6999888f6f99998f6df998f66ddf98666ddf9f666ddf9f666
# 100:a6666888aaa68999a9989999a99999886a99982266a982236698223366982334
# 101:886666f69986fff6999888f6899988f628998f66228986663228f6663328f666
# 102:a6666888aaa68999a9989999a99999886a99982266a982336698233466982344
# 103:886666f69986fff6999888f6899988f628998f66328986663328f6664328f666
# 104:0000000000200000222222220242000002200000020000000000000000000000
# 105:0000000000444000400400003443444444f40400044004000400000000000000
# 106:0000000000000000444440440044440004000044444404400000000000000000
# 107:000000000000000000bbbbb00000000000bbbbb0000000000000000000000000
# 112:66a99f2d66a999ff6aaa9999aa999999a9999996999999866999886666666666
# 113:df99f666f999f66699998f66899998f6899998f6899999f6899999f66888ff66
# 114:66a99f2d66a999ff6aaa9999aa999999a9999986a99999869999998669998866
# 115:df99f666f999f66699998f66899998f6899999f6899999f66888ff6666666666
# 116:66a8223366a982236a9a8222a9999888a9999986999999869999998669988866
# 117:3228f6662289f66622898f66889998f6899998f6899999f6899999f66888ff66
# 118:66a8233466a982336a9a8222a9999888a9999986999999869999998669988866
# 119:3328f6663289f66622898f66889998f6899998f6899999f6899999f66888ff66
# 120:000000008855888e8888588e0868000008800000080000000000000000000000
# 122:0000000000000000002233000222333000223300000000000000000000000000
# 123:0000000000000000002332000223322000233200000000000000000000000000
# </SPRITES>


# <MAP>
# 006:000000000000006137472131810000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 007:000000000000006238482232820000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 011:000000000000000000000000000000000000000000000000011100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 012:000000000000000000000000000000000041510000000000021200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 013:00000000000000000000000000000000a090900000000091a1b100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 014:404040404040404040404000000000a0a090a00000000092a2b200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 015:404040404040404040404040404040404040404040404040404040404040000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 016:404040404040404040404040404040404040404040404040404040404040000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# </MAP>

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