# SMALLEST DIFFERENCE

# time O(n^2) | space O(1)
def smallestDifference(arrayOne, arrayTwo):
    smallestFirst = arrayOne[0]
    smallestSecond = arrayTwo[0]
    current_diff = abs(arrayOne[0] - arrayTwo[0])

    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            if abs(arrayOne[i] - arrayTwo[j]) < current_diff:
                current_diff = abs(arrayOne[i] - arrayTwo[j])
                smallestFirst = arrayOne[i]
                smallestSecond = arrayTwo[j]
    return [smallestFirst, smallestSecond]


# time O(nlog(n) + O(mlog(m)) | space O(1)
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair




