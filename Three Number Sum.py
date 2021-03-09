"""
   THREE NUMBER SUM

   Write a function that takes in a non-empty array of distinct integers and an integer
   representing a target sum.The function should find all triplets in the array that sum
   up to the target sum and return a two-dimensional array of all these triplets.The
   numbers in each triplet should be ordered in ascending order,and the triplets
   themselves should be ordered in ascending order with respect to the numbers they hold.

   If no three numbers sum up to the target sum, the function should return an empty array.

   Sample Input
      array = [12, 3, 1, 2, -6, 5, -8, 6]
      target = 0

   Sample Output
      [[-8,2,6], [-8,3,5], [-6,1,5]]

"""

# time O(n^3) | space O(1)
def threeNumberSum(array, targetSum):
    array.sort()

    triplets = []
    for i in range(len(array) - 2):
        first_no = array[i]
        for j in range(i + 1, len(array) - 1):
            second_no = array[j]
            for k in range(j + 1, len(array)):
                third_no = array[k]
                if first_no + second_no + third_no == targetSum:
                    triplets.append([first_no, second_no, third_no])

    return triplets


# time O(n^2) | space O(n)
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            if array[i] + array[left] + array[right] == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif array[i] + array[left] + array[right] < targetSum:
                left += 1
            elif array[i] + array[left] + array[right] > targetSum:
                right -= 1
    return triplets
