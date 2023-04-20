import fonctions_aux

class Singe:
    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y
        self.range = 10
        
    def attaquer(self, u):
        return Dart(self.x, self.y, u.x, u.y)

class Ballon:
    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y
    
class Dart:
    def __init__(self, coord_x, coord_y, trajet_x, trajet_y):
        self.depart_x = coord_x
        self.depart_y = coord_y
        
        self.x = coord_x
        self.y = coord_y
        
        self.arrive_x = trajet_x
        self.arrive_y = trajet_y
        
    def mouvement(self):
        self.x, self.y = fonctions_aux.mouvement((self.depart_x, self.depart_y), (self.arrive_x, self.arrive_y), (self.x, self.y))
        
    def elimination(self):
        coef_x = self.arrive_x - self.depart_x
        if coef_x > 0 and self.x > self.arrive_x:
            del self
        elif coef_x < 0 and self.x < self.arrive_x:
            del self
                 
        coef_y = self.arrive_y - self.depart_y
        if coef_y > 0 and y > self.arrive_y:
            del self
        elif coef_y < 0 and y < self.arrive_y:
            del self
    
class Curseur:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.etat = 'vide'
        
    def choisirSinge(self):
        if self.x >= 200:
            self.etat = 'occupé'
            self.singe_choisi = True
            
    def placer(self):
        if self.etat == 'occupé' and self.singe_choisi:
            self.etat = 'vide'
            self.singe_choisi = False
            
            return Singe(self.x, self.y)

    
