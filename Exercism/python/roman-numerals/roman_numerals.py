def roman(numero):
    romano = ''
    codex = {1000: 'M', 900: 'CM', 500: 'D',
             400: 'CD', 100: 'C', 90: 'XC',
             50: 'L', 40: 'XL', 10: 'X',
             9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    keys = sorted(codex.keys())
    keys.reverse()
    while numero > 0:
        for x in keys:
            while numero >= x:
                romano += codex[x]
                numero -= x
    return romano
