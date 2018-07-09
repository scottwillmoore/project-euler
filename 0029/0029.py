bound = 100
terms = {a ** b for a in range(2, bound + 1) for b in range(2, bound + 1)}
print(len(terms))

