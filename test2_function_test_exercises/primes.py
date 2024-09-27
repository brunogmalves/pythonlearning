def count_primes(inter):

    primes = [2]

    if inter <= 1:
        return 0
    
    x = 3
    while x <= inter:
        for y in primes:
            if x % y == 0:
                x+=2
                break
        else:
            primes.append(x)
            x+=2
    return len(primes)

