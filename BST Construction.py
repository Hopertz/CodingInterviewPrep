"""
   Write a BST class for a Binary Search Tree.The class should support:
   - Inserting values with the insert method.

   - Removing value with the remove method; this method
     should only remove the first instance of a given value

   - Searching for values with the contains method

   Note that you can't remove values from a single-node tree.In
   other words,calling the remove method a single-node tree should simply
   not do anything.

   Each BST node has an integer value,a left child node,and a right child node.
   A node is said to be a valid BST node if and only if it satisfies the BST
   property: Its value is strictly greater than the values of every node to its
   left; its value is less than or equal to the values of every node to its right,
   and its children nodes are either valid BST nodes themselves or None / null.

   Sample Usage
     // Assume the following BST has already been created:
                10
              /   \
             5      15
            / \    /  \
           2    5 13   22
         /          \
        1           14

    // All operations below are performed sequentially.

    insert(12):
                10
              /   \
             5      15
            / \    /  \
           2    5 13   22
         /       / \
        1      12   14


    remove(10)
                12
              /   \
             5      15
            / \    /  \
           2    5 13   22
         /          \
        1           14


    contains(15): true
"""

# SOLUTION 1
# Recursive solution
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average : O(log(n)) time | O(log(n)) space
    # Worst : O(n) time | O(n) space
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

        return self

    # Average : O(log(n)) time | O(log(n)) space
    # Worst : O(n) time | O(n) space
    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    # Average : O(log(n)) time | O(log(n)) space
    # Worst : O(n) time | O(n) space
    def remove(self, value, parent=None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right

                else:
                    # this is a single node tree do nothing
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right

            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right

        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

# SOLUTION 2
# Iterative solution
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average : O(log(n)) time | O(1) space
    # Worst : O(n) time | O(1) space
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left

            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # Average : O(log(n)) time | O(1)) space
    # Worst : O(n) time | O(1) space
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True

        return False

    # Average : O(log(n)) time | O(1) space
    # Worst : O(n) time | O(1) space
    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left

                    elif currentNode.right is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.left = currentNode.left.left
                        currentNode.right = currentNode.right.right
                    else:
                        # this is a single node tree do nothing
                        pass
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break

        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value
