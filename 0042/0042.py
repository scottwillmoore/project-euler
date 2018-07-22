from os.path import realpath, dirname
from string import ascii_uppercase as alphabet
from math import sqrt

script_path = dirname(realpath(__file__))
data_path = script_path + "/" + "words.txt"
with open(data_path, "r") as file:
    words = [word.strip('"') for word in file.read().strip().split(",")]


def is_square(n):
    root = sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return True
    else:
        return False


values = (sum(alphabet.index(c) + 1 for c in word) for word in words)
results = (value for value in values if is_square(1 + 8 * value))

print(len(list(results)))
