"""
   A* Algorithm
   You're given a two-dimensional array containing @s and 1 s, where each @ represents a free space and each 1 represents an obstade (a space that cannot be
   passed through). You can think of this array as a grid-shaped graph. You're also given four integers startRow, startcol, endRow, and endCol , representing
   the positions of a start node and an end node in the graph.
   Write a function that finds the shortest path between the start node and the end node using the A* search algorithm and returns it.
   The shortest path should be returned as an array of node positions, where each node position is an array of two elements: the Crow, col] of the respective node
   in the graph. The output array should contain the start node's position, the end node's position, and all of the positions of the remaining nodes in the shortest path,
   and these node positions should be ordered from start node to end node.
   If there is no path from the start node to the end node, your function should return an empty array.
   Note that
      • From each node in the graph, you can only travel in four directions: up, left, down and right, you can't travel diagonally.
      • The distance between all neighboring nodes in the graph is the same; you can treat it as a distance of 1.
      • The start node and end node are guaranteed to be located in empty spaces (cells containing @ ).
      • The start node and end node will never be out of bounds and will never overlap.
      There will be at most one shortest path from the start node to the end node.
      If you're unfamiliar with A*, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.

   Sample Input

    startRow = 0
    startcol = 1
    endRow = 4
    endcol = 3
    graph [
       [0, 0, 0, 0, 0],
       [0, 1, 1, 1, 0],
       [0, 0, 0, 0, 0],
       [1, 0, 1, 1, 1],
       [0, 0, 0, 0, 0],
    ]

    Sample Output
       [[0, 1], [0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1], [4, 2], [4, 3]]
      // The shortest path can be clearly seen here:
       [
        [., ., 0, 0, 0],
        [., 1, 1, 1, 0],
        [., ., 0, 0, 0]
        [1,.,  1, 1, 1],
        [0, ., ., ., 0],
      ]

"""

# SOLUTION 1

class Node:
    def __init__(self, row, col, value):
        self.id = str(row) + "-" + str(col)
        self.row = row
        self.col = col
        self.value = value
        self.distanceFromStart = float("inf")
        self.estimatedDistanceToEnd = float("inf")
        self.cameFrom = None


# O(w * h * log(w * h)) time | (w * h) space where
# w is the width of the graph and h is the height
def aStarAlgorithm(startRow, startCol, endRow, endcol, graph):
    nodes = initializeNodes(graph)

    startNode = nodes[startRow][startCol]
    endNode = nodes[endRow][endcol]
    startNode.distanceFromStart = 0
    startNode.estimatedDistanceToEnd = calculateManhattanDistance(startNode, endNode)
    nodesToVisit = MinHeap([startNode])

    while not nodesToVisit.isEmpty():
        currentMinDistanceNode = nodesToVisit.remove()
        if currentMinDistanceNode == endNode:
            break

        neighbors = getNeighboringNodes(currentMinDistanceNode, nodes)
        for neighbor in neighbors:
            if neighbor.value == 1:
                continue

            tentativeDistanceToNeighbor = currentMinDistanceNode.distanceFromStart + 1
            if tentativeDistanceToNeighbor >= neighbor.distanceFromStart:
                continue
            neighbor.cameFrom = currentMinDistanceNode
            neighbor.distanceFromStart = tentativeDistanceToNeighbor
            neighbor.estimatedDistanceToEnd = tentativeDistanceToNeighbor + calculateManhattanDistance(neighbor,
                                                                                                       endNode)
            if not nodesToVisit.containsNode(neighbor):
                nodesToVisit.insert(neighbor)
            else:
                nodesToVisit.update(neighbor)
    return reconstructPath(endNode)


def initializeNodes(graph):
    nodes = []
    for i, row in enumerate(graph):
        nodes.append([])
        for j, value in enumerate(row):
            nodes[i].append(Node(i, j, value))
    return nodes


def calculateManhattanDistance(currentNode, endNode):
    currentRow = currentNode.row
    currentCol = currentNode.col
    endRow = endNode.row
    endcol = endNode.col
    return abs(currentRow - endRow) + abs(currentCol - endcol)


def getNeighboringNodes(node, nodes):
    neighbors = []
    numRows = len(nodes)
    numCols = len(nodes[0])

    row = node.row
    col = node.col
    if row < numRows - 1:  # DOWN
        neighbors.append(nodes[row + 1][col])
    # UP
    if row > 0:
        neighbors.append(nodes[row - 1][col])

    if col < numCols - 1:  # RIGHT
        neighbors.append(nodes[row][col + 1])

    # LEFT
    if col > 0:
        neighbors.append(nodes[row][col - 1])
    return neighbors


def reconstructPath(endNode):
    if not endNode.cameFrom:
        return []
    currentNode = endNode
    path = []

    while currentNode is not None:
        path.append([currentNode.row, currentNode.col])
        currentNode = currentNode.cameFrom

    return path[::-1]


class MinHeap:
    def __init__(self, array):
        # Holds the position in the heap that each node is at
        self.nodePositionsInHeap = {node.id: idx for idx, node in enumerate(array)}
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

        # O(n) time | O(1) space

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2

        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

        # O(log(n)) time | O(1) space)

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1

        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if (
                    childTwoIdx != -1
                    and heap[childTwoIdx].estimatedDistanceToEnd < heap[childOneIdx].estimatedDistanceToEnd
            ):
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap].estimatedDistanceToEnd < heap[currentIdx].estimatedDistanceToEnd:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    # O(log(n)) time | O(1) space)
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx].estimatedDistanceToEnd < heap[parentIdx].estimatedDistanceToEnd:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

            # O(log(n)) time | O(1) space)

    def remove(self):
        if self.isEmpty():
            return
        self.swap(0, len(self.heap) - 1, self.heap)
        node = self.heap.pop()
        del self.nodePositionsInHeap[node.id]
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return node

    def insert(self, node):
        self.heap.append(node)
        self.nodePositionsInHeap[node.id] = len(self.heap) - 1
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        self.nodePositionsInHeap[heap[i].id] = j
        self.nodePositionsInHeap[heap[j].id] = i
        heap[i], heap[j] = heap[j], heap[i]

    def containsNode(self, node):
        return node.id in self.nodePositionsInHeap

    def update(self, node):
        self.siftUp(self.nodePositionsInHeap[node.id], self.heap)
