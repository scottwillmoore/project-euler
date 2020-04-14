digits = {str(n) for n in range(1, 10)}
pandigitals = []

for x in range(1, 10_000):
    n = 1
    s = str(x)

    while len(s) < 9 and digits.difference(s):
        n += 1
        s += str(x * n)

    if len(s) == 9 and not digits.difference(s):
        print((x, n), s)
        pandigitals.append(int(s))

print(max(pandigitals))
