class node:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.nearest = None
        self.parent = None