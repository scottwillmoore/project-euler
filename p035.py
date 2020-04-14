def eratosthenes(n):
    sieve = [True] * n
    sieve[0:1] = [False, False]

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return {n for (n, p) in enumerate(sieve) if p}


bound = 1_000_000
evens = {"0", "2", "4", "6", "8"}
primes = eratosthenes(bound)

rotate = lambda s, i: s[i:] + s[:i]
circular = lambda s: all([int(rotate(s, i)) in primes for i in range(len(s))])

numbers = [str(n) for n in range(3, bound) if evens.isdisjoint(str(n))]

result = len([s for s in numbers if circular(s)]) + 1
print(result)
