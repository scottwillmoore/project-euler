total = 0
limit = 10_000

divisors = lambda n: [d for d in range(1, (n // 2) + 1) if n % d == 0]
proper_divisors = [divisors(n) for n in range(0, limit)]
sum_of_divisors = list(map(sum, proper_divisors))

for (n, s) in enumerate(sum_of_divisors):
    # Handle all cases where s < limit (pre-computed).
    if s < n and sum_of_divisors[s] == n:
        print((s, n))
        total += s + n

    # Handle any cases where s > limit (not pre-computed).
    # This is not actually needed for the conditions of this question.
    if s > n and s > limit:
        if n == divisors(s):
            print((s, n))
            # Only add the amicable number that is below the limit.
            total += n

print(total)