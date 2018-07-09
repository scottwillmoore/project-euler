coin_types = [200, 100, 50, 20, 10, 5, 2, 1]
target_amount = 200


# This is not the most efficient solution, however the recursive algorithm is
# extremely easy to understand and it is more than fast enough for the
# parameters of the supplied problem.
def take_coin(coins):
    total_amount = sum(coins)

    if total_amount == target_amount:
        return 1
    if total_amount > target_amount:
        return 0

    solutions = 0
    for coin in coin_types:
        if len(coins) == 0 or coin <= coins[-1]:
            solutions += take_coin(coins + [coin])
    return solutions


print(take_coin([]))
