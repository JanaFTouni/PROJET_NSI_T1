import pyxel

pyxel.init(128, 128, title="Test collision cercle")

player = (64,64)

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
    x_a, y_a = coord_1[0], coord_1[1]
    x_b, y_b = coord_2[0], coord_2[1]
    
    return (x_b-x_a)**2 + (y_b-y_a)**2
    
def update():
    global player, range
    player = player_mouvement(player)
    range = distance(player, (64,64))
    
def draw():
    pyxel.cls(0)    
    pyxel.circ(64, 64, 10, 11)
    if range <= 109:
        pyxel.circ(64, 64, 10, 8)
    
    pyxel.rect(player[0], player[1], 1, 1, 7)
        
pyxel.run(update, draw) 
