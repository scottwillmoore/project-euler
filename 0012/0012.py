def triangular_numbers():
    i, n = 1, 0
    while 1:
        n += i
        i += 1
        yield n


num_divisors = 500

# This solution is extremely slow, but works...
for num in triangular_numbers():
    i = 1
    count = 0
    while i ** 2 <= num:
        if num % i == 0:
            count += 2
        i += 1

    print(num, ",", count)

    if count > num_divisors:
        print(num)
        break
