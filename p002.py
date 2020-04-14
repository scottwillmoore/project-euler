total = 0
bound = 4_000_000

a, b = 1, 1
while a < bound:
    if a % 2 == 0:
        total += a

    a, b = b, b + a

print(total)
