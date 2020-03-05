def find(lista_de_numeros, numero):
    der, izq = 0, len(lista_de_numeros)-1
    while izq >= der:
        intermedio = (der+izq)//2
        numero_intermedio = lista_de_numeros[intermedio]
        if numero_intermedio == numero:
            return intermedio
        if numero_intermedio < numero:
            der = intermedio + 1
        else:
            izq = intermedio - 1

    raise ValueError("No encontrado.")
