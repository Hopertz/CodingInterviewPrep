"""
   Depth-First Search

   You're given Node class that has a name and and an array of optional children nodes.
   When put together,nodes form an acyclic tree-like structure.

   Implement the depthFirstSearch method on the Node class,which takes in an empty array,
   traverses the tree using the Depth-first Search approach (specifically navigating the
   tree from left to right),stores all of the nodes' names in the input array, and return
   it.

   Sample Input
      tree  =   A
              / | \
             B  C   D
            / \    /  \
           E   F  G   H
              / \  \
             I  J   K

   Sample Output
   ['A','B','E','F','I','J','C','D','G','K','H']
"""

# SOLUTION 1

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Running time O(V+E) space O(V), V-vertices E-edges
    def depthFirstSearch(self, array):
        array.append(self.name)
        childs = self.children
        if childs is None:
            return
        for child in childs:
            child.depthFirstSearch(array)

        return array
