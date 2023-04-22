import pyxel, definitions, cartes, fonctions_aux

class App:
    def __init__(self):
        pyxel.init(256, 128, title="05 Basique")
        
        self.liste_ballons = []
        self.liste_singes = []
        self.liste_darts = []
        self.curseur = definitions.Curseur()
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            ballon = definitions.Ballon(0, 30, "Jaune")
            self.liste_ballons.append(ballon)
        elif pyxel.btnp(pyxel.KEY_M):
            ballon = definitions.Ballon(0, 30, "Moab")
            self.liste_ballons.append(ballon)
            
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 200 <= self.curseur.x <= 216 and 16 <= self.curseur.y <= 32:
            self.curseur.choisirSinge()
            
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.curseur.etat != 'vide':
            singe = self.curseur.placer()
            approuve = True
            #On teste si le placement n'est pas sur un singe déjà placé
            for singe_places in self.liste_singes:
                if fonctions_aux.collision(singe_places, singe):
                    approuve = False
            if approuve:
                self.liste_singes.append(singe)
            
        cartes.carte_1(self.liste_ballons)
        self.curseur.x, self.curseur.y = pyxel.mouse_x, pyxel.mouse_y
        
        for singe in self.liste_singes:
            for ballon in self.liste_ballons:
                if fonctions_aux.distance((singe.x, singe.y),(ballon.x, ballon.y)) <= singe.range**2+singe.range and pyxel.frame_count % singe.cooldown == 0:
                    dart = singe.attaquer(ballon)
                    self.liste_darts.append(dart)
                break #On fait le singe attaquer qu'une fois
        
        for dart in self.liste_darts:
            dart.mouvement()
            if dart.elimination:
                self.liste_darts.remove(dart)
            for ballon in self.liste_ballons:
                if fonctions_aux.collision(dart, ballon):
                    ballon.vies -= dart.degats
                    dart.percer -= 1
                    if dart.percer <= 0:
                        self.liste_darts.remove(dart)
                        break
                ballon.check_elimination()
                if ballon.elimination:
                    if ballon.suivant is not None:
                        for nouveau_ballon in ballon.suivant:
                            self.liste_ballons.append(definitions.Ballon(ballon.x, ballon.y, nouveau_ballon))
                    self.liste_ballons.remove(ballon)
        
    def draw(self):
        pyxel.load("my_resource.pyxres", True, True, True, True)
        pyxel.cls(11)
        pyxel.rect(0, 30, 64, 4, 4)
        pyxel.rect(60, 30, 4, 34, 4)
        pyxel.rect(0, 60, 64, 4, 4)
        pyxel.rect(200, 0, 56, 128, 7)
        pyxel.blt(200, 16, 0, 16, 0, 16, 16, 9)
        for singe in self.liste_singes:
            #pyxel.circ(singe.x, singe.y, singe.range, 11)
            pyxel.blt(singe.x-6, singe.y-8, 0, 16, 0, singe.longueur, singe.taille, 9)
        for ballon in self.liste_ballons:
            pyxel.blt(ballon.x-6, ballon.y-8, 0, ballon.u, ballon.v, ballon.longueur, ballon.taille, 9)
        for dart in self.liste_darts:
            pyxel.blt(dart.x, dart.y, 0, dart.u, dart.v, dart.longueur, dart.taille, 9)
        if self.curseur.etat == 'vide':
            pyxel.rect(self.curseur.x, self.curseur.y, 1, 1, 6)
        elif self.curseur.etat != 'vide':
            pyxel.rect(self.curseur.x, self.curseur.y, 1, 1, 8)
        
App()
