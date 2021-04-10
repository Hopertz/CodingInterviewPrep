"""
  River Sizes

  You're given a two-dimensional array(a matrix) of potentially unequal height and width
  containing only 0 s and 1 s.Each 0 represents land, and each 1 represents part of a
  river.A river consists of any number of 1 s that are either horizontal or vertically
  adjacent (but not diagonal adjacent).The number of adjacent 1 s forming a river
  determine its size.

  Note that a river can twist.In other words,it doesn't have to be a straight vertical
  line or a straight horizontal line; it can be L-shaped, for example.

  Write a function that returns an array of the sizes of all rivers represented in the
  input matrix.The size don't need to be in any particular order.

  Sample input
     matrix = [
      [1, 0, 0, 1, 0],
      [1, 0, 1, 0, 0],
      [0, 0, 1, 0, 1],
      [1, 0, 1, 0, 1],
      [1, 0, 1, 1, 0],
  ]

  Sample Output
     [1, 2, 2, 2, 5] // The numbers could be ordered differently

     // The rivers can be clearly seen here:
     [
      [1,  ,  , 1,  ],
      [1,  , 1,  ,  ],
      [ ,  , 1,  , 1],
      [1,  , 1,  , 1],
      [1,  , 1, 1,  ],
  ]


"""

# O(N) time | O(N) space where N is the total number elements in the matrix.
def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j]:
                continue
            traverseNodes(i, j, matrix, visited, sizes)
    return sizes


def traverseNodes(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodesToExplore = [[i, j]]
    while len(nodesToExplore):
        currenNode = nodesToExplore.pop()
        i = currenNode[0]
        j = currenNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbours = getUnvisitedNeighbours(i, j, matrix, visited)
        for neighbour in unvisitedNeighbours:
            nodesToExplore.append(neighbour)

    if currentRiverSize > 0:
        sizes.append(currentRiverSize)


def getUnvisitedNeighbours(i, j, matrix, visited):
    unvisitedNeighbours = []
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbours.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbours.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbours.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbours.append([i, j + 1])

    return unvisitedNeighbours



