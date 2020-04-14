from math import sqrt


is_pentagonal = lambda x: sqrt(24 * x + 1) % 6 == 5


s = 5000
for j in range(1, s):
    pj = j * (3 * j - 1) // 2
    for k in range(j, s):
        pk = k * (3 * k - 1) // 2
        if is_pentagonal(pj + pk) and is_pentagonal(pk - pj):
            print(pk - pj)
