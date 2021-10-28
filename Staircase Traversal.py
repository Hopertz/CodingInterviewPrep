"""
  Staircase Traversal

  You're given two positive integers representing the height of a staircase and the maximum
  number of steps that you can advance up the staircase at a time.Write a function that
  returns the number of ways in which you can climb the staircase.

  For example,if you were given a staircase of height = 3 and maxSteps = 2 you could climb the
  staircase in 3 ways.You could take 1 step, 1step, then 1 step, you could also take 1 step, then
  2 steps, and you could take 2 steps,then 1 step.

  Note that maxSteps <= height will always be true.

  Sample Input
    height = 4
    maxSteps = 2

  Sample Output
    5
    // You can climb the staircase in the following ways:
    // 1, 1, 1, 1
    // 1, 1, 2
    // 1, 2, 1
    // 2, 1, 1
    // 2, 2
"""

# SOLUTION 1

# O(K^n) time | O(n) space where n is the height of the staircase and k is the number of staircase available
def staircaseTraversal(height, maxSteps):
    return numberOfWaysToTop(height, maxSteps)


def numberOfWaysToTop(height, maxSteps):
    if height <= 1:
        return 1
    numberOfWays = 0
    for step in range(1, min(maxSteps, height) + 1):
        numberOfWays += numberOfWaysToTop(height - step, maxSteps)

    return numberOfWays


# SOLUTION 2

# O(K*n) time | O(n) space where n is the height of the staircase and k is the number of staircase available
def staircaseTraversal(height, maxSteps):
    return numberOfWaysToTop(height, maxSteps, {0: 1, 1: 1})


def numberOfWaysToTop(height, maxSteps, memoize):
    if height in memoize:
        return memoize[height]
    numberOfWays = 0
    for step in range(1, min(maxSteps, height) + 1):
        numberOfWays += numberOfWaysToTop(height - step, maxSteps, memoize)

    memoize[height] = numberOfWays

    return numberOfWays

# SOLUTION 3

# O(K*n) time | O(n) space where n is the height of the staircase and k is the number of staircase available
def staircaseTraversal(height, maxSteps):
    waysToTop = [0 for _ in range(height + 1)]
    waysToTop[0] = 1
    waysToTop[1] = 1

    for currentHeight in range(2, height + 1):
        step = 1
        while step <= maxSteps and step <= currentHeight:
            waysToTop[currentHeight] = waysToTop[currentHeight] + waysToTop[currentHeight - step]
            step += 1

    return waysToTop[height]
