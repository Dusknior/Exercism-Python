def factors(value):
    cont = 2
    primes = []
    while value > 1:
        if value % cont == 0:
            value /= cont
            primes.append(cont)
        else:
            cont += 1
    return primes
