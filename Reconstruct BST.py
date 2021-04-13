"""
  Reconstruct BST

  The pre-order traversal of a Binary Tree is traversal technique that starts at the tree's root
  node and visits nodes in the following order:


      1. Current node
      2. Left subtree
      3. Right subtree

  Given a non-empty array of integers representing the pre-order traversal of a Binary Search Tree
  (BST),write a function that creates the relevant BST and returns its root node.

  The input array will contain the values of BST nodes in the order in which these nodes would be
  visited with a pre-order traversal.

  East BST node has an integer value, a left child node and a right child node. A node is said to be
  valid BST node if and only if it satisfies the BST property: its value is strictly greater than the
  values of every node to its left;its value is less than or equal to the values of every node to its
  right; and its children nodes are either valid BST nodes themselves or None / null.

  Sample Input
     preOrderTraverseValues = [10, 4, 2, 1, 5, 17, 19, 18]

  Sample Output
         10
        /  \
       4    17
      / \    \
     2   5   19
    /        /
   1        10
"""


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n^2) time | O(n) space - where n is the length of the input array
def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return None

    currentValue = preOrderTraversalValues[0]
    rightSubtreeRootIdx = len(preOrderTraversalValues)

    for idx in range(1, len(preOrderTraversalValues)):
        value = preOrderTraversalValues[idx]
        if value >= currentValue:
            rightSubtreeRootIdx = idx
            break

    leftSubtree = reconstructBst(preOrderTraversalValues[1: rightSubtreeRootIdx])
    rightSubtree = reconstructBst(preOrderTraversalValues[rightSubtreeRootIdx:])

    return BST(currentValue, leftSubtree, rightSubtree)


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx


# O(n) time | O(n) space - where n is the length of the input array
def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(float("-inf"), float("inf"), preOrderTraversalValues, treeInfo)


def reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo):
    if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
        return None

    rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]
    if rootValue < lowerBound or rootValue >= upperBound:
        return None

    currentSubtreeInfo.rootIdx += 1
    leftSubtree = reconstructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo)
    rightSubtree = reconstructBstFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubtreeInfo)

    return BST(rootValue, leftSubtree, rightSubtree)
