# The largest value a single digit can produce is 9! = 362_880.

# Using this fact we can construct this equation:
# 9! * x = 10^x => x ~ 6.36 => x < 7 [x: the number of digits]

# Now we know that these factorial sums are bounded by this inequality:
# 2 < n < 10^x < 10^7 [n: the input to the factorial sum]

# We can then brute force the solution with the following Python.

from math import factorial

factorial_lookup = {n: factorial(n) for n in range(10)}
factorial_sum = lambda n: sum([factorial_lookup[int(c)] for c in str(n)])
print(sum([n for n in range(3, 10 ** 7) if n == factorial_sum(n)]))
