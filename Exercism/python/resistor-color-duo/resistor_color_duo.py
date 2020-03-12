colores = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
           "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}


def value(colors):
    color1 = colors[0]
    color2 = colors[1]
    return int((str(colores[color1]) + str(colores[color2])))
