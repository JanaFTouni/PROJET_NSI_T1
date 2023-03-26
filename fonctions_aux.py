def distance(coord_1, coord_2):
    """Renvoie la distance entre deux objets"""
    x_a, y_a = coord_1[0], coord_1[1]
    x_b, y_b = coord_2[0], coord_2[1]
    
    return (x_b-x_a)**2 + (y_b-y_a)**2

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
    if mouv == 0:
        mouv = 1

    return (x + (coef_x/mouv), y + (coef_y/mouv))