# bound = 1_000_000
# lookup = [n ** 5 for n in range(10)]

# total = 0
# for n in range(2, bound):
#     digits = map(int, str(n))
#     powers = map(lambda n: lookup[n], digits)
#     if sum(powers) == n:
#         print(n)
#         total += n

# print(total)

# Here is the solution in a single disgusting line of Python.
# fmt: off
print(sum([n for n in range(2, 10**6) if sum(map(lambda n: n ** 5, map(int, str(n)))) == n]))
