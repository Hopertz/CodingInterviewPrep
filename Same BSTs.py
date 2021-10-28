"""
  Same BSTS

    An array of integers is said to represent the Binary Search Tree (BST) obtained by inserting each integer in
    the array, from left to right, into the BST.
    Write a function that takes in two arrays of integers and determines whether these arrays represent the
    same BST. Note that you're not allowed to construct any BSTs in your code.
    A BST is a Binary Tree that consists only of BST nodes. A node is said to be a valid BST node if and only
    if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is
    less than or equal to the values of every node to its right; and its children nodes are either valid BST
    nodes themselves or None / null.

    Sample Input
       arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
       arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]

    Sample Output
        true // both arrays represent the BST below

                10
              /    \
             8      15
            /     /  \
           5     12   94
         /      /    /
        2      11   81



"""


# SOLUTION 1

# O(n^2) time | O(n^2) space where n is the number of
# nodes in each array, respectively
def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False

    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False

    leftone = getSmaller(arrayOne)
    leftTwo = getSmaller(arrayTwo)
    rightone = getBiggerOrEqual(arrayOne)
    rightTwo = getBiggerOrEqual(arrayTwo)

    return sameBsts(leftone, leftTwo) and sameBsts(rightone, rightTwo)


def getSmaller(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller


def getBiggerOrEqual(array):
    biggerOrEqual = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            biggerOrEqual.append(array[i])
    return biggerOrEqual


# SOLUTION 2

# O(n^2) time | 0(d) space - where n is the number of
# nodes in each array, respectively, and d is the depth
# of the BST that they represent
def sameBsts(arrayOne, arrayTwo):
    return areSameBsts(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))


def areSameBsts(arrayone, arrayTwo, rootIdxone, rootIdxTwo, minval, maxval):
    if rootIdxone == -1 or rootIdxTwo == -1:
        return rootIdxone == rootIdxTwo

    if arrayone[rootIdxone] != arrayTwo[rootIdxTwo]:
        return False

    leftRootIdxone = getIdxofFirstSmaller(arrayone, rootIdxone, minval)
    leftRootIdxTwo = getIdxofFirstSmaller(arrayTwo, rootIdxTwo, minval)
    rightRootIdxone = getIdxofFirstBiggerOrEqual(arrayone, rootIdxone, maxval)
    rightRootIdxTwo = getIdxofFirstBiggerOrEqual(arrayTwo, rootIdxTwo, maxval)

    currentvalue = arrayone[rootIdxone]
    leftAreSame = areSameBsts(arrayone, arrayTwo, leftRootIdxone, leftRootIdxTwo, minval, currentvalue)
    rightAreSame = areSameBsts(arrayone, arrayTwo, rightRootIdxone, rightRootIdxTwo, currentvalue, maxval)

    return leftAreSame and rightAreSame


def getIdxofFirstSmaller(array, startingIdx, minval):
    # Find the index of the first smaller value after the startingIdx.
    # Make sure that this value is greater than or equal to the minval,
    # which is the value of the previous parent node in the BST. If it
    # isn't, then that value is located in the left subtree of the
    # previous parent node.
    for i in range(startingIdx + 1, len(array)):
        if array[startingIdx] > array[i] >= minval:
            return i
    return -1


def getIdxofFirstBiggerOrEqual(array, startingIdx, maxval):
    # Find the index of the first bigger/equal value after the startingIdx.
    # Make sure that this value is smaller than maxval, which is the value
    # of the previous parent node in the BST. If it isn't, then that value
    # is located in the right subtree of the previous parent node.
    for i in range(startingIdx + 1, len(array)):
        if array[startingIdx] <= array[i] < maxval:
            return i
    return -1
