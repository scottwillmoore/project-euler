e = 10e-6

for b in range(10, 100):
    for a in range(10, b):
        r = a / b

        a1 = a % 10
        a10 = (a // 10) % 10

        b1 = b % 10
        b10 = (b // 10) % 10

        if a1 == b1 and a1 != 0 and b1 != 0:
            c = a10
            d = b10
        elif a1 == b10:
            c = a10
            d = b1
        elif a10 == b1:
            c = a1
            d = b10
        elif a10 == b10:
            c = a1
            d = b1
        else:
            continue

        if c != 0 and d != 0:
            s = c / d
            if abs(s - r) < e:
                print(a, "/", b, "->", c, "/", d)
