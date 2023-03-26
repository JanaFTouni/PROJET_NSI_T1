def carte_1(tab: list):
    """Fait avancer dans le parcours de la première carte
    les elements de tab."""
    for elt in tab:
        
        if 0 <= elt.x <= 60 and 30 <= elt.y <= 34:
            elt.x += 1
        elif 0 <= elt.x <= 64 and 60 <= elt.y <= 64:
            elt.x -= 1
        elif 60 <= elt.x <= 64 and 30 <= elt.y <= 64:
            elt.y += 1
        elif elt.x < 0:
            elt.x, elt.y = 0, 30

