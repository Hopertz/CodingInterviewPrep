"""
   Validate Subsequence

   Given two non-empty arrays of integers,write a function that determines whether
   the second array is a subsequence of the first one.

   A subsequence of an array is a set of numbers that aren't necessarily adjacent
   in the array but that are in the same order as they appear in the array.For instance,
   the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4] and so do the numbers
   [2. 4].Note that a single number in the array and the array itself are both valid
   subsequence of the array.

   Sample Input
     array = [5, 1, 22, 25, 6, -1, 8,10]
     sequence = [1, 6 ,-1, 10]

   Sample Output
      True

"""

def validatedSub(array, subsequence):
    # time O(n) space O(1)
    seq_id = 0
    for value in array:
        if value == subsequence[seq_id]:
            seq_id += 1

        if seq_id == len(subsequence):
            return True

    return False


def validatedSub(array, subsequence):
    # time O(n) space O(1)
    arr_id = 0
    seq_id = 0
    while arr_id < len(array) and seq_id < len(subsequence):
        if array[arr_id] == subsequence[seq_id]:
            seq_id += 1
        arr_id += 1

    return len(subsequence) == seq_id


