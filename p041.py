from itertools import permutations


def is_prime(n):
    if n < 2:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True


pandigitals = []
for n in range(1, 10):
    digits = [str(n) for n in range(1, n + 1)]
    pandigitals += list(map(lambda t: int("".join(t)), permutations(digits)))

print(max(filter(is_prime, pandigitals)))
