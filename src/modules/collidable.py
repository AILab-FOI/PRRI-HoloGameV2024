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