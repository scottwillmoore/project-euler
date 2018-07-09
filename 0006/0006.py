n = 100

nums = list(range(n + 1))
sum_of_square = sum([x ** 2 for x in nums])
square_of_sum = sum(nums) ** 2

d = square_of_sum - sum_of_square

print(d)
