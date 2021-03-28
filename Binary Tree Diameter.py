"""
  Binary Tree Diameter

  Write a function that takes in a Binary Tree and returns its diameter.The diameter of a binary
  tree is defined as the length of its longest path,,even if that path doesn't pass through the
  root of the tree.

  A path is a collection of connected nodes in a tree,where no node is connected to more than
  two other nodes. The length of a path is the number of edges between the paths's first node
  and its last node.

  Each BinaryTree node node has an integer value, a left child node, and a right child node.Children
  nodes can either be BinaryTree nodes themselves or None/ null.

  Sample Input
                1
              /   \
             3      2
            / \
          7    4
         /      \
        8        5
       /          \
      9            6

    Sample Output
       6  // 9 -> 8 -> 7 -> 3 ->4 -> 5 -> 6
       // There are 6 edges between the first node and the last node of this tree's longest path.

"""


# O(n) time | O(h) space where n is the number of nodes in the binary tree
# and h is the height of the Binary tree

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currentDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
    currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return TreeInfo(currentDiameter, currentHeight)


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height
