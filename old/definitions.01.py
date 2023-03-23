class Singe:
    pass

class Ballon:
    
    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y
    
    def coords(self):
        return self.x, self.y
    
    def coord_x(self):
        return self.x
    
    def coord_y(self):
        return self.y
