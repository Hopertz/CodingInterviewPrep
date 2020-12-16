#Bubble Sort

# Solution One
# Running time O(n^2)  space 0(1)
def bubbleSort1(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def bubbleSort2(array):
    for i in range(len(array)):
        swaped = True
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swaped = False
    if swaped:
        break
    return array


def bubbleSort(array):
    issorted = False
    counter = 0
    while not issorted:
        issorted = True
        for j in range(0, len(array) - counter - 1):
            if array[j] > array[j + 1]:
               array[j], array[j + 1] = array[j + 1], array[j]

        counter += 1
    return array



