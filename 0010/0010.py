from math import log


def primes(n):
    p = [1] * n
    p[0] = p[1] = 0

    i = 2
    while i < n:
        if p[i]:
            yield i
            for j in range(2 * i, n, i):
                p[j] = 0
        i += 1


m = 2 * 10 ** 6

primes = list(primes(m))
s = sum(primes)

print(s)

