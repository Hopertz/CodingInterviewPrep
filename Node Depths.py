""""
   Node's Depth

   The distance between a node in a Binary Tree and the tree's root is called the node's
   depths.
   Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.

   Each BinaryTree node has an integer value, a left child node and a right child node.
   Children nodes can either be BinaryTree nodes themselves or None / null.

   Sample Input
      tree  =   1
              /   \
             2      3
            / \    /  \
           4    5 6   7
         / \
        8   9

   Sample Output
   16
   // The depth of the node with value 2 is 1.
   // The depth of the node with value 3 is 1
   // The depth of the node with value 4 is 2.
   // The depth of the node with value 5 is 2
   // The depth of the node with value 6 is 2.
   // The depth of the node with value 7 is 2
   // The depth of the node with value 8 is 3.
   // The depth of the node with value 9 is 3
   // Summing all of the depths yields 16
"""


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Running  time O(n) , space O(h) where n is nodes number in a binary tree,h is node's height
def nodeDepths(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


# Running time O(n) , space O(h) where n is nodes number in a binary tree,h is node's height
def nodeDepths(root):
    sumDepths = 0
    stack = [{"node": root, "depth": 0}]

    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sumDepths
