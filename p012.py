def triangular_numbers():
    k = 0
    n = 0
    while True:
        k += 1
        n += k
        yield n


def divisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i


# The generators were significantly slower than the simpler explicit approach.

# for n in triangular_numbers():
#     d = sum(1 for _ in divisors(n))
#     print(n, d)
#     if d > 500:
#         print(n, d)
#         break

k = 0
n = 0
d = 0
while not d > 500:
    k += 1
    n += k

    i = 0
    d = 0
    while i * i <= n:
        i += 1
        if n % i == 0:
            d += 2

print(n, d)
