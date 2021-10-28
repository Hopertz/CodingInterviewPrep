"""
   Breadth-first Search

   You're given a Node class that has a name and an array of optional children
   nodes.When put together,nodes form an acyclic tree-like structure.

   Implement the breadthFirstSearch method on the Node class,which takes in
   an empty array,traverses the tree using the Breadth-first Search approach
   (specifically navigating the tree from left to right), stores all of the nodes
   names in the input array,and returns it.

   Sample Input

   graph =      A
              / | \
             B  C  D
            / \   /  \
           E   F G   H
              /\  \
            I  J   K

   Sample Output
     ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K']
"""


# SOLUTION 1

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space
    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)

        return array

