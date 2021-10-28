"""
     Right Smaller Than  ☆
  Write a function that takes in an array of integers and returns an array of the same length, where each
  element in the output array corresponds to the number of integers in the input array that are to the right
  of the relevant index and that are strictly smaller than the integer at that index.
  In other words, the value at output[i] represents the number of integers that are to the right of i and
  that are strictly smaller than input[i] .

   sample Input
       array = [8, 5, 11, -1, 3, 4, 2]

   Sample Output
      [5, 4, 4, 0, 1, 1, 0]
    // There are 5 integers smaller than 8 to the right of it.
    // There are 4 integers smaller than 5 to the right of it.
    // There are 4 integers smaller than 11 to the right of it.
    // Etc..

"""

# SOLUTION 1

# O(n^2) time | 0(n) space - where n is the length of the array
def rightSmallerThan(array):
    rightSmallerCounts = []
    for i in range(len(array)):
        rightSmallerCount = 0
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                rightSmallerCount += 1
        rightSmallerCounts.append(rightSmallerCount)
    return rightSmallerCounts


# SOLUTION 2

# Average case: when the created BST is balanced
# O(nlog(n)) tine | O(n) space - where n is the length of the array
# ---
# Worst case: when the created BST is like a linked list
# O(n2) tine | O(n) space
def rightSmallerThan(array):
    if len(array) == 0:
        return []
    lastIdx = len(array) - 1
    bst = SpecialBST(array[lastIdx], lastIdx, 0)
    for i in reversed(range(len(array) - 1)):
        bst.insert(array[i], i)
    rightSmallerCounts = array[:]
    getRightSmallerCounts(bst, rightSmallerCounts)
    return rightSmallerCounts


def getRightSmallerCounts(bst, rightSmallerCounts):
    if bst is None:
        return
    rightSmallerCounts[bst.idx] = bst.numSmallerAtInsertTime
    getRightSmallerCounts(bst.left, rightSmallerCounts)
    getRightSmallerCounts(bst.right, rightSmallerCounts)


class SpecialBST:
    def __init__(self, value, idx, numSmallerAtInsertTime):
        self.value = value
        self.idx = idx
        self.numSmallerAtInsertTime = numSmallerAtInsertTime
        self.leftSubtreesize = 0
        self.left = None
        self.right = None

    def insert(self, value, idx, numSmallerAtInsertTime=0):
        if value < self.value:
            self.leftSubtreesize += 1
            if self.left is None:
                self.left = SpecialBST(value, idx, numSmallerAtInsertTime)
            else:
                self.left.insert(value, idx, numSmallerAtInsertTime)
        else:
            numSmallerAtInsertTime += self.leftSubtreesize
            if value > self.value:
                numSmallerAtInsertTime += 1
            if self.right is None:
                self.right = SpecialBST(value, idx, numSmallerAtInsertTime)
            else:
                self.right.insert(value, idx, numSmallerAtInsertTime)





# SOLUTION 3

# Average case: when the created BST is balanced
# O(nlog(n)) time | O(n) space - where n is the length of the array
# ---
# Worst case: when the created BST is like a linked list
# O(n^2) time | O(n) space
def rightSmallerThan(array):
    if len(array) == 0:
        return []

    rightSmallerCounts = array[:]
    lastIdx = len(array) - 1
    bst = SpecialBST(array[lastIdx])
    rightSmallerCounts[lastIdx] = 0
    for i in reversed(range(len(array) - 1)):
        bst.insert(array[i], i, rightSmallerCounts)

    return rightSmallerCounts


class SpecialBST:
    def __init__(self, value):
        self.value = value
        self.leftSubtreeSize = 0
        self.left = None
        self.right = None

    def insert(self, value, idx, rightSmallerCounts, numSmallerAtInsertTime=0):
        if value < self.value:
            self.leftSubtreeSize += 1
            if self.left is None:
                self.left = SpecialBST(value)
                rightSmallerCounts[idx] = numSmallerAtInsertTime
            else:
                self.left.insert(value, idx, rightSmallerCounts, numSmallerAtInsertTime)
        else:
            numSmallerAtInsertTime += self.leftSubtreeSize
            if value > self.value:
                numSmallerAtInsertTime += 1
            if self.right is None:
                self.right = SpecialBST(value)
                rightSmallerCounts[idx] = numSmallerAtInsertTime
            else:
                self.right.insert(value, idx, rightSmallerCounts, numSmallerAtInsertTime)
