total = 1

spiral_size = 1001
step_function = lambda n: 2 * ((2 * n ** 2) - (3 * n) + 3)

for n in range(3, spiral_size + 1, 2):
    total += step_function(n)

print(total)
