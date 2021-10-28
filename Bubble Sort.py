"""
   Bubble Sort

   Write a function that takes in an array of integers and returns a sorted version of that
   array.Use the Bubble Sort algorithm to sort the array.

   Sample Input
     array = [8, 5, 2, 9, 5, 6, 3]

   Sample Output
     [2, 3, 5, 5, 6, 8, 9]
"""

# SOLUTION 1

# Running time O(n^2)  space 0(1)
def bubbleSort(array):
    issorted = False
    counter = 0
    while not issorted:
        issorted = True
        for j in range(0, len(array) - counter - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                issorted = False

        counter += 1
    return array

# SOLUTION 2

# Running time O(n^2)  space 0(1)
def bubbleSort(array):
    # run  loops two times: one for walking through the array
    # and the other for comparison
    for i in range(len(array)):
        # largest element is placed at the end no need to go to the end
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# SOLUTION 3
# Running time O(n^2)  space 0(1)
def bubbleSort(array):
    for i in range(len(array)):
        is_sorted = True
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = False
        if is_sorted:
            break
    return array


