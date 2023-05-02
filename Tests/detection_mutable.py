import pyxel

pyxel.init(128, 128, title="Test collision cercle")
 
player = (64,64)
taille_player = 5
taille_cercle = 15

def player_mouvement(coord):
    x = coord[0]
    y = coord[1]
    if pyxel.btn(pyxel.KEY_D):
        if (x < 127):
            x = x + 1
    if pyxel.btn(pyxel.KEY_A):
        if (x > 0):
            x = x - 1
    if pyxel.btn(pyxel.KEY_S):
        if (y < 127):
            y = y + 1
    if pyxel.btn(pyxel.KEY_W):
        if (y > 0):
            y = y - 1
    return (x, y)

def distance(coord_1, coord_2):
    """Renvoie la distance entre deux objets"""
    global taille_player
    x_a, y_a = coord_1[0], coord_1[1]
    x_b, y_b = coord_2[0], coord_2[1]
    
    les_x = abs(x_b-x_a)**2
    les_y = abs(y_b-y_a)**2
    
    if x_a < x_b:
        les_x = abs(x_b-x_a-(taille_player-1))**2
    if y_a < y_b:
        les_y = abs(y_b-y_a-(taille_player-1))**2
        
    return les_x + les_y
    
def update():
    global player, range, taille_player, taille_cercle
    player = player_mouvement(player)
    range = distance(player, (64,64))
    print(range)
    
def draw():
    pyxel.cls(0)    
    pyxel.circ(64, 64, taille_cercle, 11)
    if range <= taille_cercle**2+taille_cercle:
        pyxel.circ(64, 64, taille_cercle, 8)
    
    pyxel.rect(player[0], player[1], taille_player, taille_player, 7)
        
pyxel.run(update, draw) 

