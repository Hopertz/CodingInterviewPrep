"""
    Sort K-Sorted Array
  Write a function that takes in a non-negative integer k and a k-sorted array of integers and returns the sorted version of
  the array. Your function can either sort the array in place or create an entirely new array.
  A k-sorted array is a partially sorted array in which all elements are at most k positions away from their sorted position.

  For example, the array [3, 1, 2, 2] is k-sorted with k = 3 , because each element in the array is at most 3
  positions away from its sorted position.

  Note that you're expected to come up with an algorithm that can sort the k-sorted array faster than in O(nlog(n)) time.

  Sample Input
      array = [3, 2, 1, 5, 4, 7, 6, 5]
      k = 3

  Sample Output
    [1, 2, 3, 4, 5, 5, 6, 7]

"""

# SOLUTION 1

# O(nlog(k)) tine | o(k) space - where n is the number
# of elements in the array and k is how far away elements
# are from their sorted position
def sortKSortedArray(array, k):
    minHeapWithKElements = MinHeap(array[: min(k + 1, len(array))])
    nextIndexToInsertElement = 0

    for idx in range(k + 1, len(array)):
        minElement = minHeapWithKElements.remove()
        array[nextIndexToInsertElement] = minElement
        nextIndexToInsertElement += 1

        currentElement = array[idx]
        minHeapWithKElements.insert(currentElement)

        while not minHeapWithKElements.isEmpty():
            minElement = minHeapWithKElements.remove()
        array[nextIndexToInsertElement] = minElement
        nextIndexToInsertElement += 1

    return array


class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        childoneIdx = currentIdx * 2 + 1

        while childoneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childoneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childoneIdx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childoneIdx = currentIdx * 2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]