"""
   Radix Sort
Write a function that takes in an array of non-negative integers and returns a sorted version of that array.
Use the Radix Sort algorithm to sort the array.

If you're unfamiliar with Radix Sort, we recommend watching the Conceptual Overview section of this
question's video explanation before starting to code.

Sample Input
  array = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]

Sample Output
  [2, 12, 65, 87, 234, 345, 654, 3008, 8762]

"""

# SOLUTION 1

# O(d*(n + b)) time | 0(n + b) space where n is the length of the input array,
# d is the max number of digits, and b is the base of the numbering system used
def radixSort(array):
    if len(array) == 0:
        return array
    maxNumber = max(array)

    digit = 0
    while maxNumber / 10 ** digit > 0:
        countingSort(array, digit)
        digit += 1

    return array

def countingSort(array, digit):
    sortedArray = [0] * len(array)
    countArray = [0] * 10

    digitColumn = 10 ** digit
    for num in array:
        countIndex = (num // digitColumn) % 10
        countArray[countIndex] += 1

    for idx in range(1, 10):
        countArray[idx] += countArray[idx - 1]

    for idx in range(len(array) - 1, -1, -1):
        countIndex = (array[idx] // digitColumn) % 10
        countArray[countIndex] -= 1
        sortedIndex = countArray[countIndex]
        sortedArray[sortedIndex] = array[idx]

    for idx in range(len(array)):
        array[idx] = sortedArray[idx]
