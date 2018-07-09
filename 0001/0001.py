condition = lambda n: n % 3 == 0 or n % 5 == 0
result = sum(filter(condition, range(0, 1000)))
print(result)