"""
      Cycle In Graph
   You're given a list of edges representing an unweighted, directed graph with at least one node. Write a function that
   returns a boolean representing whether the given graph contains a cycle.

   For the purpose of this question, a cycle is defined as any number of vertices, including just one vertex, that are
   connected in a closed chain. A cycle can also be defined as a chain of at least one vertex in which the first vertex
   is the same as the last. The given list is what's called an adjacency list, and it represents a graph.

   The number of vertices in the graph is equal to the length of edges , where each index i in edges contains vertex i's
   outbound edges, in no particular order. Each individual edge is represented by a positive integer that denotes an index
   (a destination vertex) in the list that this vertex is connected to. Note that these edges are directed, meaning that
   you can only travel from a particular vertex to its destination, not the other way around (unless the destination
   vertex itself has an outbound edge to the original vertex).

   Also note that this graph may contain self-loops. A self-loop is an edge that has the same destination and origin; in
   other words, it's an edge that connects a vertex to itself. For the purpose of this question, a self-loop is considered
   a cycle.

   Sample Input
      edges = [
       [1, 3),
       [2, 3, 4],
       [@],
       [],
       [2, 5],
       [],
      ]

    Sample Output
      true
      // There are multiple cycles in this graph:
      // 1) 0 -> 1 -> 2 -> 0
      // 2) 0 -> 1 -> 4 -> 2 -> 0
      // 3) 1 -> 2 -> -> 1
      // These are just 3 examples; there are more.


"""

# O(v + e) time | O(v) space - where v is the number of the 
# vertices and e is the number of edges in the graph.
def cycleInGraph(edges):
      numberOfNodes = len(edges)
      visited = [False for _ in range(numberOfNodes)]
      currentlyInStack = [False for _ in range(numberOfNodes)]
      
      for node in range(numberOfNodes):
            if visited[node]:
                 continue
            
            containsCycle =  isNodeInCycle(node, edges, visited, currentlyInStack)
            if containsCycle:
                  return True
            
       return False

def isNodeInCycle(node, edges, visited, currentlyInStack):
      visited[node] = True
      currentlyInStack[node] = True
      
      neighbors = edges[node]
      for neighbor in neighbors:
            if not visited[neighbor]:
                  containsCycle = isNodeInCycle(neighbor, edges, visited, currentlyInStack)
                  if containsCycle:
                        return True
            elif currentlyInStack[neighbor]:
                  return True
            
       currentlyInStack[node] = False
       return False
      
   

WHITE, GREY, BLACK = 0, 1, 2

# O(v + e) time | O(v) space - where v is the number of the 
# vertices and e is the number of edges in the graph.
def cycleInGraph(edges):
    numberOfNodes = len(edges)
    colors = [WHITE for _ in range(numberOfNodes)]
      
    for node in range(numberOfNodes):
        if colors[node] != WHITE:
           continue
                  
        containsCycle = traverseAndColorNodes(node, edges, colors)
        if containsCycle:
           return True

     return False


def traverseAndColorNodes(node, edges, colors):
    colors[node] = GREY

    neighbors = edges[node]
    for neighbor in neighbors:
        neighborColor = colors[neighbor]
            
        if neighborColor == GREY:
           return True
        
        if neighborColor == BLACK:
           continue
      
        containsCycle = traverseAndColorNodes(neighbor, edges, colors)
        if containsCycle:
            return True
      
    colors[node] = BLACK
    return False
        
        



      
                  

