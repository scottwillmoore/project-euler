from math import factorial

index = 1_000_000 - 1
num_choices = 10
choices = [str(x) for x in range(0, num_choices)]
permutation = ""

num_choices = len(choices)
while num_choices > 0:
    num_permutations = factorial(num_choices)
    choice_size = num_permutations // num_choices

    choice_index = index // choice_size
    index = index % choice_size

    permutation += choices[choice_index]
    choices.pop(choice_index)
    num_choices = len(choices)

print(permutation)
