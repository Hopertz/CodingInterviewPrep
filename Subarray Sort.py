
"""
   Subarray Sort
   
Write a function that takes in an array of at least two integers and that returns an array of the starting 
and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for 
the entire input array to be sorted (in ascending order).
If the input array is already sorted, the function should return [-1, -1] .

Sample Input
    array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

Sample Output
    [3, 9]
"""
# SOLUTION 1

# O(n) time | O(1) space
def subarraySort(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)
    if minOutOfOrder == float("inf"):
        return [-1, -1]
    subarrayLeftIdx = 0
    while minOutOfOrder >= array[subarrayLeftIdx]:
        subarrayLeftIdx += 1
    subarrayRightIdx = len(array) - 1
    while maxOutOfOrder <= array[subarrayRightIdx]:
         subarrayRightIdx -= 1
    return [subarrayLeftIdx, subarrayRightIdx]

def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]

