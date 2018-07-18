def eratosthenes(n):
    sieve = [True] * n
    sieve[0:1] = [False, False]

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [n for (n, p) in enumerate(sieve) if p]


print(eratosthenes(300))
exit()
primes = eratosthenes(1_000_000)

cases = ["2", "3", "5", "7"]

left_choices = ["1", "3", "7", "9"]
right_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def left(base):
    options = set()
    for choice in left_choices:
        case = base + choice
        if int(case) in primes:
            options.add(case)
            options = options.union(left(case))
    return options


def right(base):
    options = set()
    for choice in right_choices:
        case = choice + base
        if int(case) in primes:
            options.add(case)
            options = options.union(right(case))
    return options


a = set()
for case in cases:
    a = a.union(left(case))

b = set()
for case in cases:
    b = b.union(right(case))

print(a.intersection(b))
print(len(a.intersection(b)))
