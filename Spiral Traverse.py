# SPIRAL TRAVERSE

# Iterative solution
# time O(N) | space O(N) - where n is the total number of elements in the array
def spiralTraverse1(array):
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
def spiralTraverse2(array):
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
