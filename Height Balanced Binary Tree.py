"""
  Height Balanced Binary Tree

  You're given the root node of a Binary Tree.Write a function that returns true
  if this Binary Tree is height balanced and false if it isn't.

  A Binary Tree is height balanced if for each node in the tree,the difference
  between the height of its left subtree and the height of its right subtree
  is at most 1.

  Each BinaryTree node has an integer value,a left child node, and a right child
  node.Children nodes can either be BinaryTree nodes themselves or None/ null.

  Sample Input
  tree =   1
         /  \
        2    3
       / \    \
      4   5    6
         / \
        7   8

  Sample Output
    true

"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height


# O(n) time | O(h) space where n is the number of nodes in the tree
# h is the height of the binary of Tree
def heightBalancedBinaryTree(tree):
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced


def getTreeInfo(node):
    if node is None:
        return TreeInfo(True, -1)
    leftSubtreeInfo = getTreeInfo(node.left)
    rightSubtreeInfo = getTreeInfo(node.right)

    isBalanced = (
            leftSubtreeInfo.isBalanced
            and rightSubtreeInfo.isBalanced
            and abs(leftSubtreeInfo.height - rightSubtreeInfo.height) <= 1
    )
    height = max(leftSubtreeInfo.height, rightSubtreeInfo.height) + 1
    return TreeInfo(isBalanced, height)
