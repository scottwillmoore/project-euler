c = lambda n: n % 3 == 0 or n % 5 == 0
print(sum(filter(c, range(0, 1000))))
