from math import sqrt


is_pentagonal = lambda x: sqrt(24 * x + 1) % 6 == 5
is_hexagonal = lambda x: sqrt(8 * x + 1) % 4 == 3

i = 1
t = 1
while t < 10_000_000_000:
    if is_pentagonal(t) and is_hexagonal(t):
        print(t)
    i += 1
    t += i
