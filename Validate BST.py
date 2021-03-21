"""
  Validate a function that takes in a potentially invalid Binary Search Tree(BST) and returns
  a boolean representing whether the BST is valid.

  Each BST node has an integer value, a left child node, and a right child node.A node is sais
  to be valid BST node if and only if it satisfies the BST property:Its value is strictly greater
  than the values of every node to its left;its value is less than or equal to the values of every
  node to its right and its children nodes are either valid BST nodes themselves or None / null.

  A BST is valid if and only if all of its nodes are valid BST nodes.

   Sample Input

                10
              /   \
             5      15
            / \    /  \
           2    5 13   22
         /          \
        1           14


  Sample Output
    True
"""


# This is an input class. Do not edit.
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))

# O(n) time | O(d) space where d is longest depth of a branch
def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)
