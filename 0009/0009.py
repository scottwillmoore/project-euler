def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


for a in range(1, 500):
    b1 = 1000 * (500 - a)
    b2 = 1000 - a

    if gcd(b1, b2) == b2:
        b = b1 // b2
        c = 1000 - a - b

        print(a * b * c)
        break

