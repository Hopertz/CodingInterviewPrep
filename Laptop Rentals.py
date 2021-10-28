"""
  Laptop Rentals  ☆
 You're given a list of time intervals during which students at a school need a laptop. These time intervals are represented
 by pairs of integers [start, end] , where 0 <= start < end . However, start and end don't represent real
 times; therefore, they may be greater than 24 .
 No two students can use a laptop at the same time, but immediately after a student is done using a laptop, another
 student can use that same laptop. For example, if one student rents a laptop during the time interval [0, 2] , another
 student can rent the same laptop during any time interval starting with 2.
 Write a function that returns the minimum number of laptops that the school needs to rent such that all students will
 always have access to a laptop when they need one.

 Sample Input
  times =
   [
    [0, 2],
    [1, 4],
    [4, 6],
    [0, 4],
    [7, 8],
    [9, 11),
    [3, 10],
   ]

  Sample Output
    3

"""

# SOLUTION 1

# O(nlog(n)) time | O(n) space - where n is the number of times

def laptopRentals(times):
    if len(times) == 0:
        return 0
    usedLaptops = 0
    startTimes = sorted([interval[0] for interval in times])
    endTimes = sorted([interval[1] for interval in times])
    startIterator = 0
    endIterator = 0

    while startIterator < len(times):
        if startTimes[startIterator] >= endTimes[endIterator]:
            usedLaptops -= 1
            endIterator += 1
        usedLaptops += 1
        startIterator += 1
    return usedLaptops


# SOLUTION 2

# O(nlog(n)) time | O(n) space - where n is the number of times
def laptopRentals(times):
    if len(times) == 0:
        return 0
    times.sort(key=lambda x: x[0])
    timesWhenLaptopIsused = [times[0]]
    heap = Minheap(timesWhenLaptopIsused)

    for idx in range(1, len(times)):
        currentInterval = times[idx]
        if heap.peek()[1] <= currentInterval[0]:
            heap.remove()
        heap.insert(currentInterval)
    return len(timesWhenLaptopIsused)


class Minheap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    # O(n) time 0(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    # O(log(n)) time | 0(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childoneIdx = currentIdx * 2 + 1
        while childoneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childoneIdx][1]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childoneIdx

            if heap[idxToSwap][1] < heap[currentIdx][1]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childoneIdx = currentIdx * 2 + 1
            else:
                return

    # O(log(n)) time | 0(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx][1] < heap[parentIdx][1]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    # 0(1) time | 0(1) space
    def peek(self):
        return self.heap[0]

    # O(log(n)) time | 0(1) space
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    # O(log(n)) time | 0(1) space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
