"""
     Minimum Area Rectangle  ☆
     You're given an array of points plotted on a 2D graph (the xy-plane). Write a function that returns the minimum area of
     any rectangle that can be formed using any 4 of these points such that the rectangle's sides are parallel to the x and y
     axes (i.e., only rectangles with horizontal and vertical sides should be considered--no rectangles with diagonal sides). If
     no rectangle can be formed, your function should return O.
     The input array will contain points represented by arrays of two integers [x, y] . The input array will never contain
     duplicate points.

     Sample Input
        points =
          [
             [1, 5),
             [5, 1],
             [4, 2],
             [2, 4],
             [2, 2],
             [1, 2],
             [4, 5],
             [2, 5],
             [-1, -2],
          ]
     Sample Output
       3
     // The rectangle with corners [1, 5], [2, 5], [1, 2], and [2, 2]
     // has the minimum area: 3.

"""

# SOLUTION 1

# O(n^2) time | O(n) space - where n is the number of points
def minimumAreaRectangle(points):
    columns = initializeColumns (points)
    minimumAreaFound = float("inf")
    edgesParallelToyAxis = {}

    sortedColumns = sorted(columns.keys())
    for x in sortedColumns:
        yValuesInCurrentColumn = columns[x]
        yValuesInCurrentColumn.sort()

        for currentIdx, y2 in enumerate(yValuesInCurrentColumn):
            for previousIdx in range(currentIdx):
                y1 = yValuesInCurrentColumn[previousIdx]
                pointString = str(y1) + ":" + str(y2)
                if pointString in edgesParallelToyAxis:
                    currentArea = (x - edgesParallelToyAxis[pointString])*(y2 - y1)
                    minimumAreaFound = min(minimumAreaFound, currentArea)
                edgesParallelToyAxis[pointString] = x

    return minimumAreaFound if minimumAreaFound != float("inf") else 0

def initializeColumns (points):
    columns = {}

    for point in points:
        x, y = point
        if x not in columns:
            columns[x] = []
        columns[x].append(y)
    return columns

# SOLUTION 2

# O(n^2) time | O(n) space - where n is the number of points
def minimumAreaRectangle(points):
    pointSet = createPointSet(points)
    minimumAreaFound = float("inf")

    for currentIdx, p2 in enumerate(points):
        p2x, p2y = p2
        for previousIdx in range(currentIdx):
            plx, ply = points[previousIdx]
            pointsShareValue = plx==p2x or ply == p2y
            if pointsShareValue:
                continue
            # If (plx, p2y) and (p2x, ply), exist we've found a rectangle.
            point10nOppositeDiagonalExists = convertPointToString(plx, p2y) in pointSet
            point20nOppositeDiagonalExists = convertPointToString(p2x, ply) in pointSet
            oppositeDiagonalExists = point10nOppositeDiagonalExists and point20nOppositeDiagonalExists

            if oppositeDiagonalExists:
                currentArea = abs(p2x - plx) * abs (p2y - ply)
                minimumAreaFound = min(minimumAreaFound, currentArea)

    return minimumAreaFound if minimumAreaFound != float("inf") else 0

def createPointSet(points):
    pointSet = set()
    for point in points:
        x, y = point
        pointString = convertPointToString(x, y)
        pointSet.add(pointString)
    return pointSet

def convertPointToString(x, y):
    return str(x) + ":" + str(y)


