#class collidable:
#    def __init__(self, x, y, width, height):
#        self.x = x
#        self.y = y
#        self.width = width
#        self.height = height
#
#    def check_collision(self, other):
#        if (self.x < other.x + other.width and
#            self.x + self.width > other.x and
#            self.y < other.y + other.height and
#            self.y + self.height > other.y):
#            return True
#        return False
#
#class platforma(collidable):
#    def __init__(self, x, y, width, height):
#        super().__init__(x, y, width, height)