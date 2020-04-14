from math import sqrt
from itertools import tee

# https://docs.python.org/3/library/itertools.html#itertools-recipes
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


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


# This function only returns prime factors.
def factors(x, primes):
    if x <= 1:
        return []

    while x != 1:
        for n in primes:
            if x % n == 0:
                yield n
                x //= n
                break


# This function extends factors to reduce repeated prime factors into a single factor.
# For example: 12 = 2 * 2 * 3 = 4 * 3.
def distinct_factors(x, primes):
    if x <= 1:
        return []

    d = next(factors(x, primes))
    for n, m in pairwise(factors(x, primes)):
        if n == m:
            d *= m
        else:
            yield d
            d = m
    yield d


upper_bound = 1_000_000
consecutives = 4

memoized_primes = [n for n in primes(upper_bound)]

memoized_factors = []
for i in range(consecutives):
    memoized_factors.append(list(distinct_factors(i, memoized_primes)))

for i in range(consecutives, upper_bound):
    memoized_factors.append(list(distinct_factors(i, memoized_primes)))

    keep = True
    all_factors = set()
    for j in range(consecutives):
        n = i - j
        n_factors = memoized_factors[n]

        if len(n_factors) != consecutives:
            keep = False
            break

        all_factors.update(n_factors)

    if keep and len(all_factors) == consecutives ** 2:
        print(i - j)
        break
