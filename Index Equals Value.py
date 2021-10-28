"""
     Index Equals Value 0 ☆
   Write a function that takes in a sorted array of distinct integers and returns the first index in the array that is equal to the value at that
   index. In other words, your function should return the minimum index where index == array[index].
   If there is no such index, your function should return -1.
     Sample Input
       array = [-5, -3, 2, 3, 4, 5, 9]
     Sample Output
       3 // 3 == array[3]

"""

# SOLUTION 1

# O(log(n)) time | 0(log(n)) space where n is the length of the input array
def indexEqualsValue(array):
    return indexEqualsValueHelper (array, 0, len(array) - 1)

def indexEqualsValueHelper(array, leftIndex, rightIndex):
    if leftIndex > rightIndex:
        return -1

    middleIndex = leftIndex + (rightIndex - leftIndex) // 2
    middleValue = array[middleIndex]
    if middleValue < middleIndex:
        return indexEqualsValueHelper(array, middleIndex + 1, rightIndex)
    elif middleValue == middleIndex and middleIndex == 0:
        return middleIndex
    elif middleValue == middleIndex and array[middleIndex - 1] < middleIndex - 1:
        return middleIndex
    else:
        return indexEqualsValueHelper(array, leftIndex, middleIndex - 1)


# SOLUTION 2

# O(log(n)) time | 0(1) space - where n is the length of the input array
def indexEqualsValue(array):
    leftIndex = 0
    rightIndex = len(array) - 1
    while leftIndex <= rightIndex:
        middleIndex = leftIndex + (rightIndex - leftIndex) // 2
        middleValue = array[middleIndex]

        if middleValue < middleIndex:
            leftIndex = middleIndex + 1
        elif middleValue == middleIndex and middleIndex == 0:
             return middleIndex
        elif middleValue == middleIndex and array[middleIndex - 1] < middleIndex - 1:
            return middleIndex
        else:
            rightIndex = middleIndex - 1

    return -1

