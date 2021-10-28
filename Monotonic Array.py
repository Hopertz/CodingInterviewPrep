"""
   Monotonic Array

   Write a function that takes in array of integers and returns a boolean representing
   whether the array is monotonic.

   An array is said to be monotic if its elements, from left to right,are entirely
   non-increasing or entirely non-decreasing.

   Non-increasing elements aren't necessarily exclusively decreasing they simply don't
   increase.Similarly ,non-decreasing elements aren't necessarily increasing they simply
   don't decrease.

   Note that empty arrays and arrays of one element are monotonic.

   Sample Input
     array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

   Sample Output
       true
"""

# SOLUTION 1

# time O(n) | space O(1)
def isMonotonic(array):
    isnonedecreasing = True
    isnoneincreasing = True
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            isnoneincreasing = False
        if array[i] < array[i - 1]:
            isnonedecreasing = False

    return isnonedecreasing or isnoneincreasing


print(isMonotonic([0,0,0,0]))