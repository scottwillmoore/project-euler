n = 1000

s = 0
for i in range(1, n + 1):
    s += i ** i
d = str(s)

print(d[-10:])
