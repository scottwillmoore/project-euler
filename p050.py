from math import sqrt


def is_prime(x):
    for n in range(2, int(sqrt(x)) + 1):
        if x % n == 0:
            return False
    return True


def primes(b):
    yield 2
    for n in range(3, b, 2):
        if is_prime(n):
            yield n


b = 1_000_000
p = list(primes(b))

m = 0
l = None

for i in range(0, len(p)):
    for j in range(i + 1, len(p)):
        s = sum(p[i:j])

        # It is really just a trimmed brute-force search.
        # These three exit conditions make the search possible...

        if s >= b:
            break

        if j - i < m:
            continue

        if len(p) - i < m:
            break

        if s in p:
            if len(p[i:j]) > m:
                m = len(p[i:j])
                l = p[i:j]

print(l, m, sum(l))
