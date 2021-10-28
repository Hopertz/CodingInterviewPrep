"""
   Selection Sort

   Write a function that takes in an array of integers and returns a sorted version of that
   array.Use the Selection Sort algorithm to sort the array.

   Sample Input
     array = [8, 5, 2, 9, 5, 6, 3]

   Sample Output
     [2, 3, 5, 5, 6, 8, 9]
"""


# SOLUTION 1

# Running time O(n^2) | space 0(1)
def selectionSort(array):
    currentIndx = 0
    while currentIndx < len(array) - 1:  # Last element is already sorted.
        smallestIdx = currentIndx
        for i in range(currentIndx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i

        swap(currentIndx, smallestIdx, array)
        currentIndx += 1

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]



# SOLUTION 2

# Running time O(n^2) | space 0(1)
def selectionSort(array):
    for step in range(len(array) - 1):  # Last element is already sorted.
        min_idx = step
        for i in range(step + 1, len(array)):
            if array[i] < array[min_idx]:
                min_idx = i

        array[step], array[min_idx] = array[min_idx], array[step]

    return array


array = [8, 5, 2, 9, 5, 6, 3]
print(selectionSort(array))
