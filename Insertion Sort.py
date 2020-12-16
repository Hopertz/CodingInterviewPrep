# Insertion sort
# Running time O(n^2)  space 0(1)
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array


print(insertionSort([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))