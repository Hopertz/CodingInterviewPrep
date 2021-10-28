"""
       Two Number Sum
    Write a function that takes in a non-empty array of distinct integers and an integer
    representing a target sum.If no any two numbers in the input array sum up to the
    target sum,the function should return an empty array.

    Note that the target sum has to be obtained by summing two different integers
    in the array; you can't add a single integer to itself in order to obtain the
    target sum.

    You can assume that there will be at most one pair of numbers summing up to
    the target sum

   Sample input
      array = [3, 5,-4, 8, 11, 1, -1, 6]
      targetSum = 10

   Sample Output
      [-1, 11]

"""

# SOLUTION 1

# Time O(n^2) | Space O(1)
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        first_no = array[i]
        for j in range(i + 1, len(array)):
            second_no = array[j]
            if first_no + second_no == targetSum:
                return [first_no, second_no]
    return []


# SOLUTION 2

# Time O(n) | Space O(n)
def twoNumberSum(array, targetSum):
    # time O(n) | space O(n)
    nums = {}
    for num in array:
        potentialNum = targetSum - num
        if potentialNum in nums:
            return [potentialNum, num]
        else:
            nums[num] = True
    return []


# SOLUTION 3

# Time O(nlog(n)) | Space O(1)
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]

        elif array[left] + array[right] < targetSum:
            left += 1

        else:
            right -= 1
    return []
