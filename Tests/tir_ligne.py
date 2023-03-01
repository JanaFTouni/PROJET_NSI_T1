import pyxel, math

pyxel.init(128, 128, title="Translation")
pyxel.mouse(True)

depart = (10, 64)
arrive = (100, 64)
tir = (10, 64)

def clic():
    return (pyxel.mouse_x, pyxel.mouse_y)

def mouvement(depart, arrive, objet):
    x = objet[0]
    y = objet[1]
        
    coef_x = arrive[0] - depart[0]
    if coef_x > 0 and x > arrive[0]:
        return (depart[0], depart[1])
    elif coef_x < 0 and x < arrive[0]:
        return (depart[0], depart[1])
    
    coef_y = arrive[1] - depart[1]
    if coef_y > 0 and y > arrive[1]:
        return (depart[0], depart[1])
    elif coef_y < 0 and y < arrive[1]:
        return (depart[0], depart[1])
    
    mouv = abs(max(coef_x, coef_y))

    return (x + (coef_x/mouv), y + (coef_y/mouv))

def update():
    global depart, arrive, tir
    
    tir = mouvement(depart, arrive, tir)
    
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        depart = clic()
    elif pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
        arrive = clic()
    
def draw():
    pyxel.cls(0)
    pyxel.rect(depart[0], depart[1], 1, 1, 11)
    pyxel.rect(arrive[0], arrive[1], 1, 1, 8)
    pyxel.rect(tir[0], tir[1], 1, 1, 7)
        
pyxel.run(update, draw) 
