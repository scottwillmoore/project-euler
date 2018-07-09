n = 100

x = 1
for i in range(2, n + 1):
    x *= i

d = map(int, str(x))
s = sum(d)

print(s)
