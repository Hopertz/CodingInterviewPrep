"""
   Insertion  Sort

   Write a function that takes in an array of integers and returns a sorted version of that
   array.Use the Insertion Sort algorithm to sort the array.

   Sample Input
     array = [8, 5, 2, 9, 5, 6, 3]

   Sample Output
     [2, 3, 5, 5, 6, 8, 9]
"""

# Running time O(n^2) | space 0(1)
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array


