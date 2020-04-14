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


memoized = []
for i, n in enumerate(primes(10_000)):
    if n > 1_000:
        s = "".join(sorted(str(n)))
        memoized.append((n, i, s))

for i, ii, si in memoized:
    for j, ij, sj in memoized[ii + 1 :]:
        for k, _, sk in memoized[ij + 1 :]:
            if j - i != k - j:
                continue

            if si != sj or sj != sk:
                continue

            print(i, j, k)
