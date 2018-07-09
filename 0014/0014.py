distance_tree = { 1: 1 }
for n in range(1, 10**6):
    terms = []
    length = 1
    while n not in distance_tree:
        length += 1
        terms.append(n)

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

    length += distance_tree[n]
    for t in terms:
        if t in distance_tree:
            break

        distance_tree[t] = length
        length -= 1

initial = -1
longest = -1
for term, length in distance_tree.items():
    if length > longest:
        initial = term
        longest = length

print(initial)
