def abbreviate(frase):
    acronimo = frase.replace("'", "").title()
    return "".join(n for n in acronimo if n.isupper())
