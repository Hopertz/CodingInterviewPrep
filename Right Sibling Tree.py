"""
   Right Sibling Tree o☆
    Write a function that takes in a Binary Tree, transforms it into a Right Sibling Tree, and returns its root.
    A Right Sibling Tree is obtained by making every node in a Binary Tree have its right property point to its right sibling
    instead of its right child. A node's right sibling is the node immediately
    to its right on the same level or None / null if there is no node immediately to its right.
    Note that once the transformation is complete, some nodes might no longer have a node pointing to them. For example, in
    the sample output below, the node with value 10 no longer has any inbound pointers and is effectively unreachable.
    The transformation should be done in place, meaning that the original data structure should be mutated (no new structure
    should be created).
    Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be
    BinaryTree nodes themselves or None / null.

      Sample Input

          tree  =      1
                   /       \
                  2          3
                 / \        /  \
                4    5     6   7
              / \     \   /    / \
             8   9    10 11   12  13
                        /
                       14


        Sample Output
               1 // the root node with value 1
           /
          2----------3
         /           /
        4-----5-----6-----7
       /           /     /
      8---9     10-11 12-13 // the node with value 10 no longer has a node pointing to it
                   /
                  14
      

"""

# SOLUTION 1

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | 0(d) space - where n is the number of nodes in the Binary Tree and d is the depth (height) of the
# Binary Tree
def rightSiblingTree(root):
    mutate(root, None, None)
    return root

def mutate(node, parent, isLeftchild):
    if node is None:
        return
    left, right = node.left, node.right
    mutate(left, node, True)

    if parent is None:
        node.right = None
    elif isLeftchild:
        node.right = parent.right
    else:
        if parent.right is None:
            node.right = None
        else:
            node.right = parent.right.left
    mutate(right, node, False)

