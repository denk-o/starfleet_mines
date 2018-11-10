class mine:
    def __init__(self, x_coord, y_coord, z_dist):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.z_dist = z_dist
        self.dist = self.convertDist()
        self.is_alive = True
    def convertDist(self):
        return ord(self.z_dist) - 96
