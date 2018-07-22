from math import sqrt

perfect_squares = {n ** 2 for n in range(1, 1000)}
pythagorean_tripes = {}

# a < b < c
# a + b + c <= 1000
# a + b + sqrt(a ** 2 + b ** 2) <= 1000
# :: a < 1000
# :: b < 1000 * (a - 500) / (a - 1000)

for a in range(1, 1000):
    b_max = 1000 * (a - 500) // (a - 1000)
    for b in range(a, b_max):
        c_2 = a ** 2 + b ** 2
        if c_2 in perfect_squares:
            c = int(sqrt(a ** 2 + b ** 2))
            p = a + b + c
            pythagorean_tripes[p] = pythagorean_tripes.get(p, []) + [(a, b, c)]

perimeter_counts = {p: len(triples) for p, triples in pythagorean_tripes.items()}
result = max(perimeter_counts, key=perimeter_counts.get)
print(result)
