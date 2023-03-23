class Singe:
    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y
        self.range = 10
        
    def caser(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y
        return Singe(self.x, self.y)

class Ballon:
    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y
    
class Curseur:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.etat = 'vide'
        
    def choisirSinge(self):
        if self.x >= 200:
            self.etat = Singe(self.x, self.y)
            
    def placer(self):
        self.objet = self.etat.caser(self.x, self.y)
        self.etat = 'vide'
        return self.objet
    
