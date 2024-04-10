class collidable:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.draw_self()

    def draw_self(self):
        rect(self.x, self.y, self.width, self.height, 15)


def DefinirajKolizije():
    coll1 = collidable(20, 70, 60, 15)
    coll2 = collidable(200, 112, 40, 10)
    coll3 = collidable(150, 80, 30, 10)