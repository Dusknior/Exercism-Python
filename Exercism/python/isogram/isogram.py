def is_isogram(palabra):
    palabra_limpia = palabra.lower()
    lista_letras = []
    for letra in palabra_limpia:
        if letra.isalpha():
            if letra in lista_letras:
                return False
            lista_letras.append(letra)
    return True
