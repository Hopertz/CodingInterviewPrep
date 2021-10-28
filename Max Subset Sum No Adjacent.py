"""
  Max Subset Sum No Adjacent

  Write a function that takes in array of positive integers and returns the maximum
  sum of non-adjacent elements in the array.

  If the input array is empty ,the function should return 0.

  Sample Input
    array = [75, 105, 120, 75, 90, 135]


  Sample Output
     330 // 75 + 120 + 135
"""

# SOLUTION 1

# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
    return maxSums[-1]


# SOLUTION 2

# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first



