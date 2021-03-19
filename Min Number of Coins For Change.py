"""
  Min Number of Coins For Change

  Given an array of positive integers representing coin denominations and a single
  non-negative integer n representing a target amount of money.Write a function that
  returns the smallest number of coins needed to make change for (to sum up to) that
  target amount using the given coin denominators.

  Note that you have access to an unlimited amount of coins.In other words,if the
  denominators are [1, 5, 10], you have access to an unlimited amount of 1s, 5s and 10s

  If it's impossible to make change for the target amount, return -1.

  Sample Input
    n = 7
    denoms = [1, 5, 10]

  Sample Output
     3 // 2x1 + 1x5
"""


# time O(n*d) | space O(n) n is the length of string.
# where d is the length of denoms
def minNumberOfCoinsForChange(n, denoms):
    numOfCoins = [float('inf') for amount in range(n + 1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], numOfCoins[amount - denom] + 1)

    return numOfCoins[n] if numOfCoins[n] != float('inf') else -1


# The below solution is greedy solution it doesn't work in all cases
def minNumberOfCoinsForChange(n, denoms):
    cur = n
    denoms.sort(reverse=True)
    c = 0
    for i in denoms:
        while i <= cur:
            cur -= i
            c += 1
    return -1 if c == 0 else c
