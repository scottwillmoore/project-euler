from os.path import realpath, dirname
from copy import deepcopy

script_path = dirname(realpath(__file__))
data_path = script_path + "/triangle.txt"
with open(data_path, "r") as file:
    data = file.read().strip()

triangle = [[int(n) for n in s.split()] for s in data.splitlines()]
triangle_sum = deepcopy(triangle)

for i in range(1, len(triangle)):
    for j in range(0, len(triangle[i])):
        if j - 1 >= 0:
            left = triangle_sum[i - 1][j - 1]
        else:
            left = 0

        if j < len(triangle[i]) - 1:
            right = triangle_sum[i - 1][j]
        else:
            right = 0

        triangle_sum[i][j] += max(left, right)
    
print(max(triangle_sum[len(triangle_sum) - 1]))