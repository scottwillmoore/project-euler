grid_size = 20
grid = [[0 for x in range(grid_size + 1)] for y in range(grid_size + 1)]

for i in range(grid_size + 1):
    grid[i][0] = 1
    grid[0][i] = 1

for i in range(1, grid_size + 1):
    for j in range(1, i + 1):
        grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        grid[j][i] = grid[i][j]

print(grid[grid_size][grid_size])
