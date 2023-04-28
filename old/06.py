import pyxel, definitions, cartes, fonctions_aux

class App:
    def __init__(self):
        pyxel.init(256, 128, title="06 Upgrade + Super")
        
        self.liste_ballons = []
        self.liste_singes = []
        self.liste_darts = []
        self.curseur = definitions.Curseur()
        self.monnaie = 2000
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            ballon = definitions.Ballon(0, 30, "Jaune")
            self.liste_ballons.append(ballon)
        elif pyxel.btnp(pyxel.KEY_M):
            ballon = definitions.Ballon(0, 30, "Moab")
            self.liste_ballons.append(ballon)
        
        #Si le joueur clique sur la case d'achat d'un singe
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 200 <= self.curseur.x <= 215 and 16 <= self.curseur.y <= 31\
           and self.monnaie >= 150:
            self.curseur.ameliorer = (False, "vide")
            self.curseur.choisirSinge("Singe")
        
        #Même chose pour un super singe
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 216 <= self.curseur.x <= 231 and 16 <= self.curseur.y <= 31\
             and self.monnaie >= 1000:
            self.curseur.ameliorer = (False, "vide")
            self.curseur.choisirSinge("Super")
        
        #On place un singe
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.curseur.etat != 'vide'\
             and self.curseur.x < 200:
            singe = self.curseur.placer()
            approuve = True
            #On teste si le placement n'est pas sur un singe déjà placé
            for singe_places in self.liste_singes:
                if fonctions_aux.collision(singe_places, singe):
                    approuve = False
            if approuve:
                self.liste_singes.append(singe)
                self.monnaie -= singe.prix
            
        #On fait une amélioration d'un singe,
        #Premiere etape, choix de l'amelioration
        #Il faut qu'un singe soit choisi avant
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.curseur.ameliorer[0]:
            singe = self.curseur.ameliorer[1]
            #Le joueur choisi le chemin du haut
            if 200 <= self.curseur.x <= 215 and 100 <= self.curseur.y <= 115\
               and self.monnaie >= singe.table_ameliorations[0]:
                singe.ameliorer("top")
                if singe.ameliorations[0] <= 5:
                    self.monnaie -= singe.table_ameliorations[0]
            #Le joueur choisi le chemin du milieu
            elif 220 <= self.curseur.x <= 235 and 100 <= self.curseur.y <= 115\
               and self.monnaie >= singe.table_ameliorations[1]:
                singe.ameliorer("mid")
                if singe.ameliorations[1] <= 5:
                    self.monnaie -= singe.table_ameliorations[0]
            #Le joueur choisi le chemin du bas
            elif 240 <= self.curseur.x <= 255 and 100 <= self.curseur.y <= 115\
               and self.monnaie >= singe.table_ameliorations[2]:
                singe.ameliorer("bot")
                if singe.ameliorations[2] <= 5:
                    self.monnaie -= singe.table_ameliorations[0]
            #Pas de choix
            else:
                self.curseur.ameliorer = (False, "vide")
                
        #Deuxieme etape, choix d'un singe, si la premiere rate
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.curseur.etat == 'vide':
            for singe in self.liste_singes:
                if fonctions_aux.collision(singe, self.curseur):
                    self.curseur.ameliorer = (True, singe)
                    
        #On fait le deplacement selon la carte choisie
        cartes.carte_1(self.liste_ballons)
        self.curseur.x, self.curseur.y = pyxel.mouse_x, pyxel.mouse_y
        
        #On attaque les ballons
        for singe in self.liste_singes:
            tirs = 0
            for ballon in self.liste_ballons:
                if fonctions_aux.distance((singe.x, singe.y),(ballon.x, ballon.y)) \
                   <= singe.range**2+singe.range \
                   and pyxel.frame_count % singe.cooldown == 0:
                    dart = singe.attaquer(ballon)
                    self.liste_darts.append(dart)
                    tirs += 1
                if tirs >= singe.nb_tirs:
                    break #On fait le singe attaquer qu'une fois
        
        #On calcule les degats
        for dart in self.liste_darts:
            dart.mouvement()
            if dart.elimination:
                self.liste_darts.remove(dart)
            for ballon in self.liste_ballons:
                if fonctions_aux.collision(dart, ballon):
                    self.monnaie += (ballon.valeur * dart.degats)
                    ballon.vies -= dart.degats
                    dart.percer -= 1
                    if dart.percer <= 0:
                        self.liste_darts.remove(dart)
                        break
                ballon.check_elimination()
                if ballon.elimination:
                    if ballon.suivant is not None:
                        for nouveau_ballon in ballon.suivant:
                            self.liste_ballons.append(definitions.Ballon(ballon.x + (ballon.longueur // 2), ballon.y + (ballon.taille // 2), nouveau_ballon))
                    self.liste_ballons.remove(ballon)
        
    def draw(self):
        pyxel.load("my_resource.pyxres", True, True, True, True)
        pyxel.cls(11)
        pyxel.rect(0, 30, 64, 4, 4)
        pyxel.rect(60, 30, 4, 34, 4)
        pyxel.rect(0, 60, 64, 4, 4)
        
        #Le boutons pour faire des ameliorations
        if self.curseur.ameliorer[0]:
            singe = self.curseur.ameliorer[1]
            pyxel.circ(singe.x + (singe.longueur // 2), singe.y + (singe.taille // 2), singe.range, 3)
            pyxel.rect(200, 0, 56, 128, 7)
            pyxel.rect(199, 0, 1, 128, 0)
            pyxel.text(201, 94, f"{singe.table_a_noms[0]}", 0)
            pyxel.blt(200, 100, 0, 48, 32, 16, 16)
            pyxel.text(200, 117, f"${singe.table_ameliorations[0]}", 0)
            pyxel.text(221, 94, f"{singe.table_a_noms[1]}", 0)
            pyxel.blt(220, 100, 0, 32, 32, 16 , 16)
            pyxel.text(220, 117, f"${singe.table_ameliorations[1]}", 0)
            pyxel.text(241, 94, f"{singe.table_a_noms[2]}", 0)
            pyxel.blt(240, 100, 0, 16, 32, 16, 16)
            pyxel.text(240, 117, f"${singe.table_ameliorations[2]}", 0)
        else:
            #Aucun singe est choisi pour etre ameliorer
            pyxel.rect(200, 0, 56, 128, 7)
            pyxel.rect(199, 0, 1, 128, 0)
            pyxel.rect(200, 100, 16, 16, 0)
            pyxel.text(200, 117, "$???", 0)
            pyxel.rect(220, 100, 16, 16, 0)
            pyxel.text(220, 117, "$???", 0)
            pyxel.rect(240, 100, 16, 16, 0)
            pyxel.text(240, 117, "$???", 0)
            
        pyxel.text(201, 1, f"$:{self.monnaie}", 0)
        
        #On dessine le choix d'achat d'un simple singe
        pyxel.rect(200, 16, 16, 16, 12)
        pyxel.blt(200, 16, 0, 16, 0, 16, 16, 9)
        pyxel.text(201, 33, "150", 0)
        
        #On dessine le choix d'achat d'un super singe
        pyxel.rect(216, 16, 16, 16, 5)
        pyxel.blt(216, 16, 0, 64, 48, 16, 16, 9)
        pyxel.text(216, 33, "1000", 0)
            
        for singe in self.liste_singes:
            pyxel.blt(singe.x, singe.y, 0, singe.u, singe.v, singe.longueur, singe.taille, 9)
        for ballon in self.liste_ballons:
            pyxel.blt(ballon.x, ballon.y, 0, ballon.u, ballon.v, ballon.longueur, ballon.taille, 9)
        for dart in self.liste_darts:
            pyxel.blt(dart.x, dart.y, 0, dart.u, dart.v, dart.longueur, dart.taille, 9)
            
        #On dessine en dernier le curseur
        if self.curseur.etat == 'vide':
            pyxel.rect(self.curseur.x, self.curseur.y, self.curseur.longueur, self.curseur.taille, 6)
        elif self.curseur.etat != 'vide':
            pyxel.rect(self.curseur.x, self.curseur.y, self.curseur.longueur, self.curseur.taille, 8)
        
App()
