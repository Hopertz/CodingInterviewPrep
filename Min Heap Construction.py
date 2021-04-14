"""
   Min Heap Construction

   Implement a MinHeap class that supports

   - Building a Min Heap from an input array of integers
   - Insert integers in the heap
   - Removing the heaps's minimum/root value.
   - Peeking at the heap's minimum / root value
   - Shifting integers up and down the heap, which is to be used when inserting and removing values.

   Note that the heap should be represented in the form of an array.

   Sample Usage

   array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]

   // All operations below are performed sequentially.
   MinHeap(array) : - // instantiate a MinHeap (calls the buildHeap method and populates the heap)
   buildingHeap(array): [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
   insert(76):  [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
   peek(): -5
   remove(): -5 [2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]
   peek(): 2
   remove(): 2  [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 24, 41, 48]
   peek(): 6
   insert(87):  [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 24, 41, 48, 87]
"""


# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    # O(n) time | O(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    # O(log(n)) time | O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    # O(log(n)) time | O(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    # O(1) time | O(1) space
    def peek(self):
        return self.heap[0]

    # O(log(n)) time | O(1) space
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    # O(log(n)) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
