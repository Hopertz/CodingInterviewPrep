"""
  Number Of Binary Tree Topologies
  Write a function that takes in a non-negative integer n and returns the number of possible Binary Tree topologies
  that can be created with exactly n nodes.

  A Binary Tree topology is defined as any Binary Tree configuration, irrespective of node values. For instance,
  there exist only two Binary Tree topologies when n is equal to 2 :a root node with a left node, and a root node with a right node.
  Note that when n is equal to there's one topology that can be created: the None / null node.

  Sample Input
     n = 3
  Sample Output
  5

"""
# SOLUTION 1

# Upper Bound: 0((n* (2n)!)/(n!(n+1)!)) time | O(n) space
def numberOfBinaryTreeTopologies(n):
    if n == 0:
        return 1
    numberOfTrees = 0
    for leftTreeSize in range(n):
        rightTreeSize = n - 1 - leftTreeSize
        numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize)
        numberOfRightTrees = numberOfBinaryTreeTopologies (rightTreeSize)
        numberOfTrees += numberOfLeftTrees * numberOfRightTrees
    return numberOfTrees

# SOLUTION 2

# O(n^2) time | (n) space
def numberOfBinaryTreeTopologies(n, cache={0: 1}):
    if n in cache:
        return cache[n]
    numberOfTrees = 0
    for leftTreeSize in range(n):
        rightTreeSize = n - 1 - leftTreeSize
        numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize, cache)
        numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize, cache)
        numberOfTrees += numberOfLeftTrees * numberOfRightTrees
    cache[n] = numberOfTrees
    return numberOfTrees

# SOLUTION 3

# O(n^2) time | O(n) space
def numberOfBinaryTreeTopologies(n):
    cache = [1]
    for m in range(1, n + 1):
        numberOfTrees = 0
        for leftTreeSize in range(m):
            rightTreeSize = m - 1 - leftTreeSize
            numberOfLeftTrees = cache[leftTreeSize]
            numberOfRightTrees = cache[rightTreeSize]
            numberOfTrees += numberOfLeftTrees * numberOfRightTrees
        cache.append(numberOfTrees)
    return cache[n]


