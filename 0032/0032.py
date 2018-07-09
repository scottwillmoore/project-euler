products = set()
required_digits = set("123456789")

for x in range(1, 100):
    for y in range(100, 10_000):
        z = x * y
        concat = str(x) + str(y) + str(z)
        digits = set(concat)
        if len(concat) == 9 and not required_digits.difference(digits):
            print(x, y, z)
            products.add(z)

print(products)
print(sum(products))
