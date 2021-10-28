"""
   Find Kth Largest Value In BST

   Write a function that takes in a Binary Search Tree(BST) and a positive integer k and returns the kth
   largest integer contained in the BST.

   You can assume that there will only be integer values in the BST and that k is less than or equal to
   the number of nodes in the tree.

   Also,for the purpose of this question ,duplicate integers will be treated as distinct values.In other
   words,the second largest value in a BST containing values {5, 7, 7} will be 7 - not 5.

   Each BST node has an integer value, a left child node, and a right child node.A node is said to be a
   valid BST node if and only if it satisfies the BST property: its value is less than or equal to the
   values of every node to its left; its value is less than or equal to the values of every node to its
   right; and its children nodes are either valid BST nodes themselves or None / null.

   Sample Input
     tree =     15
              /   \
             5      20
            / \    /  \
           2    5 17   22
         /  \
        1    3

    k = 3

    Sample Output
       17

"""

# SOLUTION 1

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def findKthLargestValueInBst(tree, k):
    inorderArray = inOrderTraverse(tree, [])
    indx = len(inorderArray) - k
    return inorderArray[indx]


def inOrderTraverse(tree, array):
    if tree is None:
        return
    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)

    return array


# SOLUTION 2

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
        self.numerOfNodesVisisted = numberOfNodesVisited
        self.latestVisitedNodeValue = latestVisitedNodeValue


# O(h + k) time | O(h) space - where h is the height of the tree and k is the input parameter
def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraverse(tree, k, treeInfo)

    return treeInfo.latestVisitedNodeValue


def reverseInOrderTraverse(node, k, treeInfo):
    if node is None or treeInfo.numerOfNodesVisisted >= k:
        return
    reverseInOrderTraverse(node.right, k, treeInfo)
    if treeInfo.numerOfNodesVisisted < k:
        treeInfo.numerOfNodesVisisted += 1
        treeInfo.latestVisitedNodeValue = node.value
        reverseInOrderTraverse(node.left, k, treeInfo)
