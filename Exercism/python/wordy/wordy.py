operadores = {'plus': '+', 'minus': '-',
              'multiplied by': '*', 'divided by': '/'}


def answer(string: str):
    string = string[8:-1]
    if string == '':
        raise ValueError('Error Encontrado')
    for keys, values in operadores.items():
        string = string.replace(keys, values)
    expression = string.split()
    try:
        if len(expression) % 2 == 0:
            raise ValueError('Error Encontrado')
        while len(expression) >= 3:
            expression[:3] = [str(eval(' '.join(expression[:3])))]
        return eval(expression[0])
    except (SyntaxError, NameError):
        raise ValueError('Error Encontrado')
