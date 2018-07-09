def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


n = 20
x = 1
for i in range(2, n + 1):
    x = lcm(x, i)

print(x)

