def lerp(a, b, t):
    return (1-t)*a + t*b

class Pogled:
    x = 0
    y = 0
    w = 240
    h = 136

    def prati(self, objekt):
        self.x = objekt.x - (self.w - objekt.width)/2
        #self.y = objekt.y - (self.h - objekt.height)/2

    def pratiIgraca(self):
        lerpSnaga = 0.05
        lerpSnagaHoda = 0.2
        ispredStoji = 6
        ispredHoda = 16
        if player.is_walking:
            self.x = lerp(self.x, player.x - (self.w - player.width)/2 + ispredHoda*int(player.desno == True) - ispredHoda*int(player.desno == False), lerpSnagaHoda)
        else:
            self.x = lerp(self.x, player.x - (self.w - player.width)/2 + ispredStoji*int(player.desno == True) - ispredStoji*int(player.desno == False), lerpSnaga)

pogled = Pogled()