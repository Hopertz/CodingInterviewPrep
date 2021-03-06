"""
   Selection Sort

   Write a function that takes in an array of integers and returns a sorted version of that
   array.Use the Selection Sort algorithm to sort the array.

   Sample Input
     array = [8, 5, 2, 9, 5, 6, 3]

   Sample Output
     [2, 3, 5, 5, 6, 8, 9]
"""


# Running time O(n^2) | space 0(1)
def selectionSort(array):
    for step in range(len(array)):
        min_idx = step
        for i in range(step + 1, len(array)):
            if array[i] < array[min_idx]:
                min_idx = i

        array[step], array[min_idx] = array[min_idx], array[step]

    return array



