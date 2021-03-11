"""
   Sorted Square Array

   Write a function that takes in non-empty array of integers that are sorted
   in ascending order and returns a new array of the same length with the squares
   of the original integers also sorted im ascending order.

   Sample Input
     array = [1 ,2 ,3, 5, 6, 8, 9]

   Sample Output
     [1 , 4, 9, 25, 36, 64, 81]
"""

# O(nlogn) time | O(n) space - where n is the length of the input array.
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]

    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value

    sortedSquares.sort()
    return sortedSquares

# O(n) time | O(n) space - where n is the length of the input array.
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1

        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1

    return sortedSquares


