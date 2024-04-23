class collidable:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #self.draw_self()

    def check_collision(self, other):
        if self.x < other.x + other.width and self.x + self.width > other.x and self.y < other.y + other.height and self.y + self.height > other.y:
            return True
        return False

    def check_collision_rectangle(self, xleft, ytop, xright, ybottom):
        if self.x < xright and self.x + self.width > xleft and self.y < ybottom and self.y + self.height > ytop:
            return True
        return False

    def draw_self(self):
        rect(self.x - int(pogled.x), self.y - int(pogled.y), self.width, self.height, 15)


def DefinirajKolizije():
    collidables = []

    tile_size = 8
    px = min(max(int(player.x/tile_size) - 5, 0), 239)
    py = min(max(int(player.y/tile_size) - 5, 0), 135)
    xrepeat = 12
    yrepeat = 12

    for xx in range(xrepeat):
        for yy in range(yrepeat):
            tileHere = mget(xx + px, yy + py)
            if tileHere != 0:
                collidables.append(collidable((xx + px)*tile_size, (yy + py)*tile_size, tile_size, tile_size))

    return collidables