"""
   Heap Sort  ♡
   Write a function that takes in an array of integers and returns a sorted version of that array. Use the Heap Sort algorithm
   to sort the array.
   If you're unfamiliar with Heap Sort, we recommend watching the Conceptual Overview section of this question's video
   explanation before starting to code.

   Sample Input
     array = [8, 5, 2, 9, 5, 6, 3]

   Sample Output
     [2, 3, 5, 5, 6, 8, 9]

"""
# SOLUTION 1

# Best: O(nlog(n)) time | 0(1) space
# Average: O(nlog(n)) time | 0(1) space
# Worst: O(nlog(n)) time | 0(1) space
def heapSort(array):
    buildMaxHeap(array)
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array)
        siftDown(0, endIdx - 1, array)
    return array

def buildMaxHeap(array):
    firstParentIdx = (len(array) - 2) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(array) - 1, array)

def siftDown(currentIdx, endIdx, heap):
    childoneIdx = currentIdx * 2 + 1
    while childoneIdx <= endIdx:
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childoneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childoneIdx
        if heap[idxToSwap] > heap[currentIdx]:
            swap(currentIdx, idxToSwap, heap)
            currentIdx = idxToSwap
            childoneIdx = currentIdx * 2 + 1
        else:
            return


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

