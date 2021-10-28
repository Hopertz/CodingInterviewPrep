"""
   Number of Ways To Make Change

   Given an array of distinct positive integers representing coin denominations
   and a single non-negative integer n representing a target amount of money.Write
   a function that returns the number of ways to make change for that target amount
   using the given coin denominations.

   Note that an unlimited amount of coins is at your disposal.

   Sample Input
     n = 6
     denoms  = [1, 5]

   Sample Output
      2 // 1x1 + 1x5 and 6x1
"""

# SOLUTION 1

# O(nd) time | O(n) space where d is the number of denoms
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]

    return ways[n]

