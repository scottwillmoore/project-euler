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


p = list(primes(100))
l = []

for n in p:
    if n < 10:
        continue

    d10 = n // 10 % 10
    d1 = n % 10

    l.append([d10, d1])

l1 = sorted(l, key=lambda x: x[1])

for x in l1:
    print(x)

print()

l10 = sorted(l, key=lambda x: x[0])

for x in l10:
    print(x)
