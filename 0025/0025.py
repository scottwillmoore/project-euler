num_digits = 1000

i = a = b = 1
while len(str(a)) < num_digits:
    i, a, b = i + 1, b, a + b

print(i)
