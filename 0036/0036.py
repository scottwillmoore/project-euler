bound = 1_000_000

palindrome = lambda s: s == s[::-1]

base2 = lambda n: palindrome(f"{n:b}")
base10 = lambda n: palindrome(f"{n}")

result = sum([n for n in range(bound) if base2(n) and base10(n)])
print(result)
