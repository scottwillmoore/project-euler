def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


lower, upper = 99, 999
largest = -1

for i in range(upper, lower, -1):
    for j in range(i, lower, -1):
        p = i * j
        if p > largest and is_palindrome(p):
            largest = p

print(largest)
