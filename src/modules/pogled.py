class Pogled:
    x = 0
    y = 0
    w = 240
    h = 136

    def prati(self, objekt):
        self.x = objekt.x - (self.w - objekt.width)/2
        #self.y = objekt.y - (self.h - objekt.height)/2

pogled = Pogled()