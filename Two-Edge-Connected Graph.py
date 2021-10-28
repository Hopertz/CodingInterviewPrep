"""
      Two-Edge-Connected Graph
   You're given a list of edges representing an unweighted and undirected graph. Write a function that returns a boolean representing
   whether the given graph is two-edge-connected.
   A graph is connected if, for every pair of vertices in the graph, there's a path of one or more edges connecting the given vertices. A graph
   that isn't connected is said to be disconnected.
   Agraph is two-edge-connected if, for every one of its edges, the edge's removal from the graph doesn't cause the graph to become
   disconnected. If the removal of any single edge disconnects the graph, then it isn't two-edge-connected. If the given graph is already
   disconnected, then it also isn't two-edge-connected. An empty graph is considered two-edge-connected.
   The input list is what's called an adjacency list, and it represents a graph. The number of vertices in the graph is equal to the length of
   edges , where each index i in edges contains vertex i 's outbound edges, in no particular order. Each outbound edge is
   represented by a positive integer that denotes an index (a destination vertex) in the list that this vertex is connected to. Note that these
   edges are undirected, meaning that you can travel from a particular vertex to its destination and from the destination back to that
   vertex. Since these edges are undirected, if vertex i has an outbound edge to vertex j , then vertex j is guaranteed to have an
   outbound edge to vertex i . For example, an undirected graph with two vertices and one edge would be represented by the following
   adjacency list edges = [[1], [0]].
   Note that the input graph will never contain parallel edges (edges that share the same source and destination vertices). In other words,
   there will never be more than one edge that connects the same two vertices to each other.

     Sample Input
        edges = [
          [1, 2, 5],
          [0, 2],
          [0, 1, 3],
          [2, 4, 5],
          [3, 5],
          [0, 3, 4],
        ]

     Sample Output
     true

"""

# SOLUTION 1

# O(v + e) time | 0(v) space - where v is the number of
# vertices and e is the number of edges in the graph
def twoEdgeConnectedGraph(edges):
    if len(edges) == 0:
        return True
    arrivalTimes = [-1] * len(edges)
    startVertex = 0

    if getMinimumArrivalTimeOfAncestors(startVertex, -1, 0, arrivalTimes, edges) == -1:
        return False

    return areAllverticesVisited(arrivalTimes)


def areAllverticesVisited(arrivalTimes):
    for time in arrivalTimes:
        if time == -1:
            return False
    return True


def getMinimumArrivalTimeOfAncestors(currentVertex, parent, currentTime, arrivalTimes, edges):
    arrivalTimes[currentVertex] = currentTime
    minimumArrivalTime = currentTime
    for destination in edges[currentVertex]:
        if arrivalTimes[destination] == -1:
            minimumArrivalTime = min(
                minimumArrivalTime,
                getMinimumArrivalTimeOfAncestors(destination, currentVertex, currentTime + 1, arrivalTimes, edges),
            )
        elif destination != parent:
            minimumArrivalTime = min(minimumArrivalTime, arrivalTimes[destination])

    # A bridge was detected, which means the graph isn't two-edge-connected.
    if minimumArrivalTime == currentTime and parent != -1:
        return -1
    return minimumArrivalTime
