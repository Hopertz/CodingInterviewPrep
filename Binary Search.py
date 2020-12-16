# Binary Search

# Solution one
# time O(logn)  space O(1)
def binarySearch1(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > array[mid]:
            left = mid + 1
        elif target < array[mid]:
            right = mid - 1
        else:
            return mid
    return -1


# Solution Two
# time O(logn)  space O(logn)
def binarySearch2(array, target):
    # Write your code here.
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

