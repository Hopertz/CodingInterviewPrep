"""
  Smallest Difference

  Write a function that takes in two non-empty arrays of integers,finds the pair of numbers
  (one from each array) whose absolute difference is closest to zero,and returns an array
  containing these two numbers,with the number from the first array in the first position.

  Note that the absolute difference of two integers is the distance between them on the
  real number line.For example,the absolute difference of -5 and 5 is 10, and the absolute
  difference of -5 and -4 is 1.

  You can assume that there will only be one pair of numbers with the smallest.

  Sample Input
      arrayOne = [-1, 5, 10 ,20, 28, 3]
      arrayTwo = [26, 134, 135, 15, 17]

  Sample Output
    [28,26]

"""

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




