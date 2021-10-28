"""
   Count Inversions  ☆
  Write a function that takes in an array of integers and returns the number of inversions in the array. An inversion
  occurs if for any valid indices i and j. i<j and array[i] > array[j] .
  For example, given array = [3, 4, 1, 2] , there are 4 inversions. The following pairs of indices represent inversions:
     [0, 2], [0, 3], [1, 2], [1, 3]
  Intuitively, the number of inversions is a measure of how unsorted the array is.

  Sample Input
     array = [2, 3, 3, 1, 9, 5, 6]

  Sample Output
    5
  // The following pairs of indices represent inversions:
  // [0, 3], [1, 3], [2, 3], [4, 5], [4, 6]

"""

# SOLUTION 1

# O(nlogn) time | O(n) space where n is the length of the array
def countInversions (array):
    return countSubArrayInversions (array, 0, len(array))

def countSubArrayInversions (array, start, end):
    if end - start <= 1:
        return 0
    middle = start + (end - start) // 2
    leftInversions = countSubArrayInversions (array, start, middle)
    rightInversions = countSubArrayInversions(array, middle, end)
    mergedArrayInversions = mergeSortAndCountInversions(array, start, middle, end)
    return leftInversions + rightInversions + mergedArrayInversions

def mergeSortAndCountInversions (array, start, middle, end):
    sortedArray = []
    left = start
    right = middle
    inversions = 0

    while left < middle and right < end:
        if array[left] <= array[right]:
            sortedArray.append(array[left])
            left += 1
        else:
            inversions += middle - left
            sortedArray.append(array[right])
            right += 1
    sortedArray += array[left:middle] + array[right:end]
    for idx, num in enumerate(sortedArray):
        array[start + idx] = num

    return inversions
