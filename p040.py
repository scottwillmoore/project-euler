decimal = "."
for n in range(1, 1_000_000):
    decimal += str(n)

result = 1
for n in range(7):
    print(n, 10 ** n, int(decimal[10 ** n]))
    result *= int(decimal[10 ** n])

# It's too easy to brute force many of these problems.
# Even with a brute force approach it still takes just over a second to execute.
print(result)
