from os.path import realpath, dirname

script_path = dirname(realpath(__file__))
data_path = script_path + "/grid.txt"
with open(data_path) as fp:
    rows = fp.read().strip()
    grid = [[int(col) for col in row.split()] for row in rows.split("\n")]

num_adj = 4
grid_size = 20
directions = ["H", "V", "D+", "D-"]

product = -1
for row in range(grid_size):
    for col in range(grid_size):

        adjs = {key: [] for key in directions}
        max_size = grid_size - num_adj
        min_size = num_adj

        for i in range(num_adj):
            if row <= max_size:
                adjs["H"].append(grid[col][row + i])
            if col <= max_size:
                adjs["V"].append(grid[col + i][row])
            if row <= max_size and col <= max_size:
                adjs["D+"].append(grid[col + i][row + i])
            if row >= min_size and col <= max_size:
                adjs["D-"].append(grid[col + i][row - i])

        for _, adj in adjs.items():
            if adj:
                result = 1
                for n in adj:
                    result *= n

                if result > product:
                    product = result

print(product)
