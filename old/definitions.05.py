import fonctions_aux, math

class Singe:
    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y
        
        self.range = 30
        self.cooldown = 30
        
        self.longueur = 16
        self.taille = 16
        
    def attaquer(self, u):
        return Dart(self.x, self.y, u.x, u.y, self.range)

class Ballon:
    def __init__(self, coord_x, coord_y, nom):
        self.x = coord_x
        self.y = coord_y
        
        self.couleur = nom
        self.elimination = False
        
        #Configuration normales pour les Bloons simples
        self.longueur = 12
        self.taille = 16
        self.vies = 1
        self.v = 16
        
        if nom == "Rouge":
            self.u = 18
            self.suivant = None
            
        elif nom == "Bleu":
            self.u = 2
            self.suivant = ["Rouge"]
            
        elif nom == "Vert":
            self.u = 34
            self.suivant = ["Bleu"]
            
        elif nom == "Jaune":
            self.u = 50
            self.suivant = ["Vert"]
            
        elif nom == "Rose":
            self.u = 178
            self.suivant = ["Jaune"]
            
        elif nom == "Noir":
            self.u = 114
            self.suivant = ["Rose", "Rose"]
            
        elif nom == "Blanc":
            self.u = 162
            self.suivant = ["Rose", "Rose"]
            
        elif nom == "Violet":
            self.u = 210
            self.suivant = ["Rose", "Rose"]
            
        elif nom == "Zebra":
            self.u = 98
            self.suivant = ["Noir", "Blanc"]
            
        elif nom == "Arc-en-ciel":
            self.u = 82
            self.suivant = ["Zebra", "Zebra"]
            
        elif nom == "Plomb":
            self.u = 194
            self.suivant = ["Noir", "Noir"]
            
        elif nom == "Ceramique":
            self.u = 130
            self.vies = 10
            self.suivant = ["Arc-en-ciel", "Arc-en-ciel"]
            
        elif nom == "Moab":
            self.u = 0
            self.v = 117
            self.vies = 200
            self.suivant = ["Ceramique", "Ceramique", "Ceramique", "Ceramique"]
            self.longueur = 34
            self.taille = 21
            
    def check_elimination(self):
        if self.vies <= 0:
            self.elimination = True
            
    def __repr__(self):
        return f"{self.couleur}"
    
class Dart:
    def __init__(self, coord_x, coord_y, trajet_x, trajet_y, range_limite):
        self.depart_x = coord_x
        self.depart_y = coord_y
        
        self.x = coord_x
        self.y = coord_y
        
        self.arrive_x = trajet_x
        self.arrive_y = trajet_y
        
        self.range = range_limite
        self.elimination = False
        
        #Dart 13x5
        self.longueur = 13
        self.taille = 5
        
        #Coordonnées dans l'editeur
        self.u = 16
        self.v = 48
        
        self.percer = 3
        self.degats = 1
        
    def mouvement(self):
        self.x, self.y = fonctions_aux.mouvement((self.depart_x, self.depart_y), (self.arrive_x, self.arrive_y), (self.x, self.y))
        self.correction_angle()
        self.check_elimination()
        
    def check_elimination(self):
        coef_x = self.arrive_x - self.depart_x
        if coef_x > 0 and math.sqrt(fonctions_aux.distance((self.depart_x, self.depart_y), (self.x, self.y))) > self.range:
            self.elimination = True
            
        elif coef_x < 0 and math.sqrt(fonctions_aux.distance((self.depart_x, self.depart_y), (self.x, self.y))) > self.range:
            self.elimination = True
            
        coef_y = self.arrive_y - self.depart_y
        if coef_y > 0 and math.sqrt(fonctions_aux.distance((self.depart_x, self.depart_y), (self.x, self.y))) > self.range:
            self.elimination = True
        
        elif coef_y < 0 and math.sqrt(fonctions_aux.distance((self.depart_x, self.depart_y), (self.x, self.y))) > self.range:
            self.elimination = True
            
        if self.percer <= 0:
            self.elimination = True
            
    def correction_angle(self):
        """On corrige le dart pour aller à la direction attendue"""
        coef_x = self.arrive_x - self.depart_x
        coef_y = self.arrive_y - self.depart_y
        
        if coef_x < 0 and self.longueur > 0:
            self.longueur = -self.longueur

        if coef_y > 0 and self.taille < 0:
            self.taille = -self.taille
            
class Curseur:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.etat = 'vide'
        
    def choisirSinge(self):
        if 200 <= self.x <= 216 and 16 <= self.y <= 32:
            self.etat = 'occupé'
            self.singe_choisi = True
            
    def placer(self):
        if self.etat == 'occupé' and self.singe_choisi:
            self.etat = 'vide'
            self.singe_choisi = False
            
            return Singe(self.x, self.y)

    
