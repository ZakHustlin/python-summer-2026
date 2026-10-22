def is_prime(n, primes):
    for prime in primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            return False
    return True

def prime(number):
    if number <= 0:
        raise ValueError('there is no zeroth prime')
    primes = []
    n = 2
    x = True
    while x is True:
        if is_prime(n, primes) is True:
            primes.append(n)
        n += 1
        if len(primes) == number:
            x = False
            break
    return primes[-1]