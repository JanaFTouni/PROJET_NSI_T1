import pyxel, definitions, cartes

class App:
    def __init__(self):
        pyxel.init(128, 128, title="01 Mouvement Ballon")
        
        self.liste_ballons = []
        
        pyxel.run(self.update, self.draw)
        
    def update(self):        
        if pyxel.btnp(pyxel.KEY_SPACE):
            a = definitions.Ballon(0, 30)
            self.liste_ballons.append(a)
        cartes.carte_1(self.liste_ballons)
        
    def draw(self):        
        pyxel.cls(0)
        pyxel.rect(0, 30, 64, 4, 4)
        pyxel.rect(60, 30, 4, 34, 4)
        pyxel.rect(0, 60, 64, 4, 4)
        for ballon in self.liste_ballons:
            pyxel.rect(ballon.x, ballon.y, 1, 1, 7)
        
App()
