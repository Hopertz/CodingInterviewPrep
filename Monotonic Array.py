# MONOTONIC ARRAY

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