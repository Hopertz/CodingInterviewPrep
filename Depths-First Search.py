# Depth First Search
# Running time O(V+E) space O(V), V-vertice E-edges

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        self.finder(array)
        return array

    def finder(self, array):
        array.append(self.name)
        childs = self.children
        if childs is None:
            return
        for child in childs:
            child.depthFirstSearch(array)
