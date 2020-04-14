from math import sqrt


def is_prime(x):
    for n in range(2, int(sqrt(x)) + 1):
        if x % n == 0:
            return False
    return True


upper_bound = 10_000

primes = [p for p in range(3, upper_bound, 2) if is_prime(p)]
squares = [s * s for s in range(1, int(sqrt(upper_bound)))]

i = 1
while i < upper_bound:
    i += 2
    if i not in primes:
        f = False
        for p in primes:
            if p > i:
                print(i)
                exit()

            for s in squares:
                if s > i:
                    break

                if i == p + 2 * s:
                    f = True
                    break

            if f:
                break
