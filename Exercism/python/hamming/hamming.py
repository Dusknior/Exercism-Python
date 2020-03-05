def distance(strand_x, strand_y):
    if len(strand_x) != len(strand_y):
        raise ValueError("La información introducida debe tener las misma longitud.")
    return sum(1 for (a,b) in zip(strand_x, strand_y) if a!=b)