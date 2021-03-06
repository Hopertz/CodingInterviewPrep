"""
   Binary Search

   Write a function that takes in a sorted array of the integers as well as a target.
   The function should use the Binary search algorithm to determine if the target integer
   is contained in the array and should return its index if it is ,otherwise -1.

   Sample Input
     array = [0, 1, 21, 33, 45, 61, 71, 72, 72, 73]
     target = 33

   Sample Output
     3
"""

# Running time O(logn) | space O(1)
def binarySearch1(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:  # or left > right
        mid = (left + right) // 2
        if target > array[mid]:
            left = mid + 1
        elif target < array[mid]:
            right = mid - 1
        else:
            return mid
    return -1


# time O(logn) | space O(logn)
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if target > array[mid]:
        return binarySearchHelper(array, target, mid + 1, right)
    elif target < array[mid]:
        return binarySearchHelper(array, target, left, mid - 1)
    else:
        return mid

