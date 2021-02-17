# Non-Constructible Change

# O(nlogn) time | O(1) space where n is the number of coins
def nonConstructibleChange(coins):
    coins.sort()

    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1

        currentChangeCreated += coin

    return currentChangeCreated + 1



