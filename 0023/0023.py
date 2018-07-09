total = 0
limit = 28_124
divisors = lambda n: [d for d in range(1, (n // 2) + 1) if n % d == 0]

abundant_numbers = {}
for n in range(0, limit):
    s = sum(divisors(n))
    if s > n:
        abundant_numbers[n] = True

for n in range(0, limit):
    b = True
    for a in abundant_numbers:
        if n - a in abundant_numbers:
            b = False

    if b:
        print(n)
        total += n

print(total)
