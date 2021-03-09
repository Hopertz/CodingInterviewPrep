"""
   Spiral Traverse

   Write a function that takes in an xm two-dimensional array(that can be square-shaped
   when n==m) and returns a one-dimensional array of all array's elements in spiral order,

   Spiral order starts at the top left corner of the two-dimensional array,goes to the
   right and proceeds in a spiral pattern all the way until every element has been visited.

   Sample Input
      array = [
        [1,   2,  3,  4]
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9,  8,  7],
      ]

   Sample Output
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

"""

# Iterative solution
# time O(N) | space O(N) - where n is the total number of elements in the array
def spiralTraverse(array):
    result = []
    startrow, endrow = 0, len(array) - 1
    startcol, endcol = 0, len(array[0]) - 1

    while (startrow <= endrow) and (startcol <= endcol):
        for col in range(startcol, endcol + 1):
            result.append(array[startrow][col])

        for row in range(startrow + 1, endrow + 1):
            result.append(array[row][endcol])

        for col in reversed(range(startcol, endcol)):
            if startrow == endrow:
                break
        result.append(array[endrow][col])

        for row in reversed(range(startrow + 1, endrow)):
            if startcol == endcol:
                break
        result.append(array[row][startcol])

        startrow += 1
        endrow -= 1
        startcol += 1
        endcol -= 1

    return result


# Recursive solution
# time O(N) | space O(N) - where n is the total number of elements in the array
def spiralTraverse(array):
    result = []
    spiral(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result


def spiral(array, startrow, endrow, startcol, endcol, result):
    if startrow > endrow or startcol > endcol:
        return

    for col in range(startcol, endcol + 1):
        result.append(array[startrow][col])

    for row in range(startrow + 1, endrow + 1):
        result.append(array[row][endcol])

    for col in reversed(range(startcol, endcol)):
        if startrow == endrow:
            break
        result.append(array[endrow][col])

    for row in reversed(range(startrow + 1, endrow)):
        if startcol == endcol:
            break
        result.append(array[row][startcol])

    spiral(array, startrow + 1, endrow - 1, startcol + 1, endcol - 1, result)
