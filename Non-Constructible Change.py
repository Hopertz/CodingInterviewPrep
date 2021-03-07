"""
  Non-Constructible Change

  Given an array of positive integers representing the values of coins in your
  possession,write a function that returns the minimum amount of change(the minimum sum
  of money) that you cannot create.Yhe given coins can have any positive integer value
  and aren't necessarily unique (i.e you can have multiple coins and of the same value).

  For example,if you're given coins = [1, 2, 5], the minimum amount of change that you
  can't create is 4. If you're given no coins,the minimum amount of change that you can't
  create is 1.

  Sample Input
    coins = [5, 7, 1, 2, 3 , 22]

  Sample Output
     20

"""


# O(nlogn) time | O(1) space where n is the number of coins
def nonConstructibleChange(coins):
    coins.sort()

    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1

        currentChangeCreated += coin

    return currentChangeCreated + 1


