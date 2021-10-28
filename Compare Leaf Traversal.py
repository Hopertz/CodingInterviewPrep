"""
     Compare Leaf Traversal
   Write a function that takes in the root nodes of two Binary Trees and returns a boolean representing whether their
   leaf traversals are the same.
   The leaf traversal of a Binary Tree traverses only its leaf nodes from left to right. A leaf node is any node that
   has no left or right children.
   For example, the leaf traversal of the following Binary Tree is 1, 3, 2.
      tree  =      4
                /   \
               1      5
                    /  \
                   3   2

   Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes
   themselves or None / null.

   Sample Input
          tree1  =   1
                   /   \
                  2      3
                 / \      \
                4    5    6
                    / \
                   7   8

           tree2  =   1
                    /   \
                   2      3
                  / \      \
                 4    7    5
                          / \
                         8   6


   Sample Output
      true

"""


# SOLUTION 1

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n + m) time | (h1 + h2) space where n is the number of nodes in the first
# Binary Tree, m is the number in the second, hi is the height of the first Binary
# Tree, and h2 is the height of the second
def compareLeafTraversal(tree1, tree2):
    tree1TraversalStack = [tree1]
    tree2TraversalStack = [tree2]

    while len(tree1TraversalStack) > 0 and len(tree2TraversalStack) > 0:
        tree1Leaf = getNextLeafNode(tree1TraversalStack)
        tree2Leaf = getNextLeafNode(tree2TraversalStack)

        if tree1Leaf.value != tree2Leaf.value:
            return False

    return len(tree1TraversalStack) == 0 and len(tree2TraversalStack) == 0

def getNextLeafNode(traversalStack):
    currentNode = traversalStack.pop()
    while not isLeafNode(currentNode):
        if currentNode.right is not None:
            traversalStack.append(currentNode.right)
        # We purposely add the left node to the stack after the
        # right node so that it gets popped off the stack first.
        if currentNode.left is not None:
            traversalStack.append(currentNode.left)

        currentNode = traversalStack.pop()

    return currentNode
def isLeafNode(node):
    return node.left is None and node.right is None



# SOLUTION 2

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n + m) time | 0(max(h1, h2)) space where n is the number of nodes in the first
# Binary Tree, m is the number in the second, hi is the height of the first Binary
# Tree, and h2 is the height of the second
def compareLeafTraversal(tree1, tree2):
    treelLeafNodesLinkedList, _ = connectLeafNodes(tree1)
    tree2LeafNodesLinkedList, _ = connectLeafNodes(tree2)

    list1CurrentNode = treelLeafNodesLinkedList
    list2CurrentNode = tree2LeafNodesLinkedList
    while list1CurrentNode is not None and list2CurrentNode is not None:
        if list1CurrentNode.value != list2CurrentNode.value:
            return False
        list1CurrentNode = list1CurrentNode.right
        list2CurrentNode = list2CurrentNode.right
    return list1CurrentNode is None and list2CurrentNode is None

def connectLeafNodes(currentNode, head=None, previousNode=None):
    if currentNode is None:
        return head, previousNode

    if isLeafNode(currentNode):
        if previousNode is None:
            head = currentNode
        else:
            previousNode.right = currentNode
        previousNode = currentNode
    leftHead, leftPreviousNode = connectLeafNodes(currentNode.left, head, previousNode)
    return connectLeafNodes(currentNode.right, leftHead, leftPreviousNode)

def isLeafNode(node):
    return node.left is None and node.right is None



