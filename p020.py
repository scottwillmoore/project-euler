from functools import reduce

n = 100
x = reduce(lambda a, x: a * x, range(2, n + 1))
print(sum(map(int, str(x))))
