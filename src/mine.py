class mine:
    def __init__(self, x_coord, y_coord, z_dist, row, col):
        self.x = x_coord
        self.y = y_coord
        self.z_dist = z_dist
        self.dist = self.convertToDist()
        self.is_alive = True
        self.row = row
        self.col = col
    def convertToDist(self):
        #since we can't use unicode conversion we just define our own dict to convert distances
        z = {}
        for ch in range(97, 123):
            z[chr(ch)] = ch-96
        for ch in range(65,91):
            z[chr(ch)] = ch-38

        return z[self.z_dist]
    def convertToChar(self):
        ch = {}
        for val in range(1,27):
             ch[val] = chr(val+96)
        for val in range(27, 53):
            ch[val] = chr(val+38)
        self.z_dist = ch[self.dist]
