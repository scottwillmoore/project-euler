from os.path import realpath, dirname

script_path = dirname(realpath(__file__))
data_path = script_path + "/names.txt"
with open(data_path) as fp:
    names_text = fp.read()

names = names_text.split(",")
names = list(map(lambda s: s[1:-1], names))
names.sort()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lookup = {c: i + 1 for i, c in enumerate(alphabet)}

total = 0
for i, name in enumerate(names):
    score = 0
    for letter in name:
        score += lookup[letter]
    total += score * (i + 1)

print(total)
