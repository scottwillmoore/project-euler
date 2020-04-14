def eratosthenes(n):
    sieve = [True] * n
    sieve[0:1] = [False, False]

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [n for (n, p) in enumerate(sieve) if p]


primes = {p: True for p in eratosthenes(2000)}
candidates = []
quadratic = lambda a, b, n: n ** 2 + a * n + b

# First create a list of potential (a, b) candidates.
# We know that for n = 0 => f = b and therefore b must be prime.
# We know that for n = 1 => f = 1 + a + b and therefore 1 + a + b must be prime.
# Using this knowledge we can reduce the search space.
for b in range(-1000, 1000 + 1):
    if b in primes:
        for a in range(-999, 999 + 1):
            if 1 + a + b in primes:
                candidates.append((a, b))

# Find the largest chain of prime numbers from the potential candidate functions.
largest = (-1, -1, -1)
for a, b in candidates:
    n = 0
    while quadratic(a, b, n) in primes:
        n += 1

    if n > largest[2]:
        largest = (a, b, n)

print(largest)
print(largest[0] * largest[1])
