a = []
for d in range(1, 1000):
    n = 1
    l = []
    m = {}

    r = n % d
    while r != 0 and r not in m:
        m[r] = len(l)

        r = r * 10

        q = r // d
        l.append(q)

        r = r % d

    if r != 0:
        a.append((d, len(l[m[r] :])))

print(max(a, key=lambda x: x[1])[0])
