from itertools import permutations

p = [2, 3, 5, 7, 11, 13, 17]

s = 0
for n in map(list, permutations(x for x in range(0, 9 + 1))):
    f = True
    for i in range(2, 8 + 1):
        d = n[i - 1] * 100 + n[i] * 10 + n[i + 1]
        if d % p[i - 2] != 0:
            f = False
            break

    if f:
        s += int("".join(map(str, n)))

print(s)
