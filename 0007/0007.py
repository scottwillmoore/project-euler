from math import log


def primes(n):
    sieve = [1] * n
    sieve[0] = sieve[1] = 0

    i = 2
    while i < n:
        if sieve[i]:
            yield i
            for j in range(2 * i, n, i):
                sieve[j] = 0
        i += 1


n = 10001

limit = int(n * log(n * log(n)))
primes = list(primes(limit))
prime = primes[n]

print(prime)
