from os.path import realpath, dirname

script_path = dirname(realpath(__file__))
data_path = script_path + "/digits.txt"
with open(data_path, "r") as file:
    data = file.read().strip().replace("\n", "")
    digits = list(map(int, data))

num_adj = 13
largest = -1
for i in range(len(digits) - num_adj + 1):
    adj = digits[i : i + num_adj]

    product = 1
    for n in adj:
        product *= n

    if product > largest:
        largest = product

print(largest)
