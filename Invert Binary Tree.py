"""
  Invert Binary Tree

  Write a function that takes in a Binary Tree and inverts it.In other words,the function
  should swap every left node in the tree for its corresponding right node.

  Each BinaryTree node has an integer value, a left child node, and a right child node.
  Children nodes can either be BinaryTree nodes themselves or None/null.

  Sample Input
      tree  =   1
              /   \
             2      3
            / \    /  \
           4    5 6   7
         / \
        8   9

  Sample Output

      tree  =   1
              /   \
             3     2
            / \    /  \
           7   6  5   4
                     /  \
                    9    8
"""


# Recursive
# O(n) time | O(d) space where d is longest depth of a branch
def invertBinaryTree(tree):
    if tree is None:
        return
    if tree:
        tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Iterative
# O(n) time | O(n)
def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
           continue
        current.left, current.right = current.right, current.left
        queue.append(current.left)
        queue.append(current.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
