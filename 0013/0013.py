from os.path import realpath, dirname

script_path = dirname(realpath(__file__))
data_path = script_path + "/numbers.txt"

numbers = []
with open(data_path) as fp:
    for ln in fp:
        numbers.append(int(ln.strip()))

# Python makes this question way too easy!
s = sum(numbers)
d = str(s)[:10]

print(d)
