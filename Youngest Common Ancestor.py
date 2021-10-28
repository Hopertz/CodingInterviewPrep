"""
  Youngest Common Ancestor

  You're given three inputs,all of which are instances of an AncestralTree class
  that have an ancestor property pointing to their youngest ancestor.The first input
  is the top ancestor in an ancestral tree(i.e, the only instance that has no ancestor
  --its ancestor property points to None / null), and the other two points are descendants
  in the ancestral tree.

  Write a function that returns the youngest common ancestor to the two descendants.

  Note that a descendant is considered its own ancestor.So in the simple ancestral tree
  below,the youngest common ancestor to nodes A amd B is node A

  // The youngest common ancestor to nodes A and B is node A
      A
     /
    B

  Sample Input
     // The nodes are from ancestral tree below.
     topAncestor = node A
     descendantOne = node E
     descendantTwo = node I
                A
              /   \
             B      C
            / \    / \
           D   E  F   G
          /\
         H  I

  Sample Output
     node B
"""

# SOLUTION 1

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# O(d) time | O(1) space where d is the depth(height) of the ancestral tree
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)


def getDescendantDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth


def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant


