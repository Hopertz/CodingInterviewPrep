"""
   Find the closest Value in BST

   Write a function that takes in a Binary Search Tree(BST) and a target integer value
   and returns the closest value to that target value contained in the BST.

   You can assume that there will only be one closest value.

   Each BST node has an integer value, a left  child node, and a right child node.
   A node is said to be a valid BST node if and only if it satisfies the BST property:
   Its value is strictly greater than the values of every node to its left; its value
   is less than or equal to the values of every node to its right and its children nodes
   are either valid BST nodes themselves or None / null.

   Sample Input
      tree  =  10
              /   \
             5     15
            / \    / \
           2   5  13  22
         /         \
        1          14

      target = 12

    Sample Output
     13
"""

# Using Recursion
# time - O(log(n))  | space - O(log(n)) because of frames in call stack
def findclosestvalueSub(tree, target):
    return closestvaluebstfinder(tree, target, tree.value)


def closestvaluebstfinder(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return closestvaluebstfinder(tree.left, target, closest)
    elif target > tree.value:
        return closestvaluebstfinder(tree.right, target, closest)
    else:
        return closest


# Using while Loop
# time - O(log(n)) | space - O(1)
def findclosestvalueBst(tree, target):
    return closestvalueBst(tree, target, tree.value)


def closestvalueBst(tree, target, closest):
    current_node = tree
    while current_node is not None:
        if abs(target - closest) > abs(target - tree.value):
            closest = tree.value
        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break
    return closest
