import pyxel, definitions, cartes

class App:
    def __init__(self):
        pyxel.init(256, 128, title="02 Placement Singe")
        
        self.liste_ballons = []
        self.liste_singes = []
        self.curseur = definitions.Curseur()
        pyxel.run(self.update, self.draw)
        
    def update(self):        
        if pyxel.btnp(pyxel.KEY_SPACE):
            ballon = definitions.Ballon(0, 30)
            self.liste_ballons.append(ballon)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.curseur.x >= 200:
            self.curseur.choisirSinge()
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.curseur.etat != 'vide':
            singe = self.curseur.placer()
            self.liste_singes.append(singe)
        cartes.carte_1(self.liste_ballons)
        self.curseur.x, self.curseur.y = pyxel.mouse_x, pyxel.mouse_y
        
        
    def draw(self):        
        pyxel.cls(0)
        pyxel.rect(0, 30, 64, 4, 4)
        pyxel.rect(60, 30, 4, 34, 4)
        pyxel.rect(0, 60, 64, 4, 4)
        pyxel.rect(200, 0, 56, 128, 7)
        for singe in self.liste_singes:
            pyxel.circ(singe.x, singe.y, singe.range, 11)
            pyxel.rect(singe.x, singe.y, 1, 1, 4)
        for ballon in self.liste_ballons:
            pyxel.rect(ballon.x, ballon.y, 1, 1, 7)
        if self.curseur.etat == 'vide':
            pyxel.rect(self.curseur.x, self.curseur.y, 1, 1, 6)
        elif self.curseur.etat != 'vide':
            pyxel.rect(self.curseur.x, self.curseur.y, 1, 1, 8)
        
App()

