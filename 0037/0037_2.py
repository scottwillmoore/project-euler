def eratosthenes(n):
    sieve = [True] * n
    sieve[0:1] = [False, False]

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return {n for (n, p) in enumerate(sieve) if p}


primes = eratosthenes(1_000_000)


def check_left(s):
    if int(s) in primes:
        if len(s) > 1:
            return check_left(s[:-1])
        else:
            return True
    else:
        return False


def check_right(s):
    if int(s) in primes:
        if len(s) > 1:
            return check_right(s[1:])
        else:
            return True
    else:
        return False


total = 0
for i in primes:
    s = str(i)
    if check_left(s) and check_right(s) and len(s) > 1:
        print(s)
        total += int(s)

print()
print(total)
