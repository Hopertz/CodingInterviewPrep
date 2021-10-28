"""
    Longest Increasing Subsequence
  Given a non-empty array of integers, write a function that returns the longest strictly-increasing subsequence in the
  array.
  A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same
  order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array
  [1, 2, 3, 4] , and so do the numbers [2, 4] . Note that a single number in an array and the array itself are both
  valid subsequences of the array.
  You can assume that there will only be one longest increasing subsequence.

    Sample Input
       array = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]

    Sample Output
      [-24, 2, 3, 5, 6, 35]

"""

# SOLUTION 1

# O(n^2) time | O(n) space
def longestIncreasingSubsequence(array):
    sequences = [None for x in array]
    lengths = [1 for x in array]
    maxlengthIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and lengths[j] + 1 >= lengths[i]:
                lengths[i] = lengths[j] + 1
                sequences[i] = j
        if lengths[i] >= lengths[maxlengthIdx]:
            maxlengthIdx = i
    return buildSequence(array, sequences, maxlengthIdx)

def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed( sequence))


# SOLUTION 2

# O(nlogn) time | O(n) space
def longestIncreasingSubsequence(array):
    sequences = [None for x in array]
    indices = [None for x in range(len(array) + 1)]
    length = 0
    for i, num in enumerate(array):
        newLength = binarySearch(1, length, indices, array, num)
        sequences[i] = indices[newLength - 1]
        indices [newLength] = i
        length = max(length, newLength)
    return buildSequence(array, sequences, indices[length])

def binarySearch(startIdx, endIdx, indices, array, num):
    if startIdx > endIdx:
        return startIdx
    middleIdx = (startIdx + endIdx) // 2
    if array[indices[middleIdx]] < num:
        startIdx = middleIdx + 1
    else:
        endIdx = middleIdx - 1
    return binarySearch(startIdx, endIdx, indices, array, num)
def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed( sequence))
