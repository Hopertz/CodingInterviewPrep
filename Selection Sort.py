# Selection sort

# Running time O(n^2) | space 0(1)
def selectionSort(array):
    for step in range(len(array)):
        min_idx = step
        for i in range(step + 1, len(array)):
            if array[i] < array[min_idx]:
                min_idx = i

        array[step], array[min_idx] = array[min_idx], array[step]

    return array


print(selectionSort([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
