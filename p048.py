n = 1000
s = 0
for i in range(1, n + 1):
    s += i ** i

print(str(s)[-10:])
