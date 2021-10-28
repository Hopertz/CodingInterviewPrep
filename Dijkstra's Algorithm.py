"""
   Dijkstra's Algorithm
   You're given an integer start and a list edges of pairs of integers.
   The list is what's called an adjacency list, and it represents a graph.
   The number of vertices in the graph is equal to the length of edges , where each index i in edges contains
   vertex i 's outbound edges, in no particular order.
   Each individual edge is represented by an pair of two numbers, [destination, distance] , where the destination is a
   positive integer denoting the destination vertex and the distance is a positive integer representing the length of
   the edge (the distance from vertex i to vertex destination ). Note that these edges are directed, meaning that
   you can only travel from a particular vertex to its destination—not the other way around (unless the destination
   vertex itself has an outbound edge to the original vertex).
   Write a function that computes the lengths of the shortest paths between start and all of the other vertices in
   the graph using Dijkstra's algorithm and returns them in an array. Each index i in the output array should represent
   the length of the shortest path between start and vertex i . If no path is found from start to vertex i ,
   then output[i] should be -1 .
   Note that the graph represented by edges won't contain any self-loops (vertices that have an outbound edge to themselves)
   and will only have positively weighted edges (i.e., no negative distances).

   If you're unfamiliar with Dijkstra's algorithm, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.

   Sample Input
     start = 0
     edges = [
           [[1, 7]],
           [[2, 6], [3, 20], [4, 3]],
           [[3, 14]],
           [[4, 2]],
           [],
           [],
           ]

   Sample Output
        [0, 7, 13, 27, 10, -1]

"""

# SOLUTION 1

# O(v^2 + e) time | 0(v) space - where v is the number of
# vertices and e is the number of edges in the input graph
def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)
    minDistances = [float("inf") for _ in range(numberOfVertices)]
    minDistances[start] = 0

    visited = set()
    while len(visited) != numberOfVertices:
        vertex, currentMinDistance = getVertexWithMinDistance(minDistances, visited)
        if currentMinDistance == float("inf"):
            break
        visited.add(vertex)
        for edge in edges[vertex]:
            destination, distanceToDestination = edge

            if destination in visited:
                continue

            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]
            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance
    return list(map(lambda x: -1 if x == float("inf") else x, minDistances))


def getVertexWithMinDistance(distances, visited):
    currentMinDistance = float("inf")
    vertex = -1
    for vertexIdx, distance in enumerate(distances):
        if vertexIdx in visited:
            continue
        if distance <= currentMinDistance:
            vertex = vertexIdx
            currentMinDistance = distance
    return vertex, currentMinDistance


# SOLUTION 2

# 0((v + e) log(v)) time | 0(v) space where v is the number
# of vertices and e is the number of edges in the input graph
def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)

    minDistances = [float("inf") for _ in range(numberOfVertices)]
    minDistances[start] = 0

    minDistancesHeap = MinHeap([(idx, float("inf")) for idx in range(numberOfVertices)])
    minDistancesHeap.update(start, 0)

    while not minDistancesHeap.isEmpty():
        vertex, currentMinDistance = minDistancesHeap.remove()

        if currentMinDistance == float("inf"):
            break

        for edge in edges[vertex]:
            destination, distanceToDestination = edge

            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]
            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance
                minDistancesHeap.update(destination, newPathDistance)

    return list(map(lambda x: -1 if x == float("inf") else x, minDistances))


class MinHeap:
    def __init__(self, array):
        # Holds the position in the heap that each vertex is at
        self.vertexMap = {idx: idx for idx in range(len(array))}
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    # O(n) time | 0(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)

        return array

    # O(log(n)) time | 0(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childoneIdx = currentIdx * 2 + 1
        while childoneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childoneIdx][1]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childoneIdx
            if heap[idxToSwap][1] < heap[currentIdx][1]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childoneIdx = currentIdx * 2 + 1
            else:
                return

    # O(log(n)) time | 0(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx][1] < heap[parentIdx][1]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    # O(log(n)) time | 0(1) space
    def remove(self):
        if self.isEmpty():
            return

        self.swap(0, len(self.heap) - 1, self.heap)
        vertex, distance = self.heap.pop()
        self.vertexMap.pop(vertex)
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return vertex, distance

    def swap(self, i, j, heap):
        self.vertexMap[heap[i][0]] = j
        self.vertexMap[heap[j][0]] = i
        heap[i], heap[j] = heap[j], heap[i]

    def update(self, vertex, value):
        self.heap[self.vertexMap[vertex]] = (vertex, value)
        self.siftUp(self.vertexMap[vertex], self.heap)
