"""
  Maximize Expression
  Write a function that takes in an array of integers and returns the largest possible value for the expression
  array[a] - array[b] + array[c] - array[d] , where a, b, c, and d are indices of the array
  and a < b <c<d.
  If the input array has fewer than 4 elements, your function should return o.
     Sample Input
        array = [3, 6, 1, -3, 2, 7]

     Sample Output
        4
        // Choose a = 1, b = 3, C = 4, and d = 5
        // -> 6 - (-3) + 2 - 7 = 4

"""

# SOLUTION 1

# O(n^4) time | 0(1) space - where n is the length of the array
def maximizeExpression(array):
    if len(array) < 4:
        return 0
    maximumvalueFound = float("-inf")
    for a in range(len(array)):
        avalue = array[a]
        for b in range(a + 1, len(array)):
            bvalue = array[b]
            for c in range(b + 1, len(array)):
                cValue = array[c]
                for d in range(c + 1, len(array)):
                    dvalue = array[d]
                    expressionValue = evaluateExpression(avalue, bvalue, cValue, dvalue)
                    maximumvalueFound = max(expressionValue, maximumvalueFound)

    return maximumvalueFound


def evaluateExpression(a, b, c, d):
    return a - b + c - d


# SOLUTION 2

# O(n) time | O(n) space where n is the length of the array
def maximizeExpression(array):
    if len(array) < 4:
        return 0

    maxOfA = [array[0]]
    maxOfAMinusB = [float("-inf")]
    maxOfAMinusBPlusC = [float("-inf")] * 2
    maxOfAMinusBPlusCMinusD = [float("-inf")] * 3

    for idx in range(1, len(array)):
        currentMax = max(maxOfA[idx - 1], array[idx])
        maxOfA.append(currentMax)

    for idx in range(1, len(array)):
        currentMax = max(maxOfAMinusB[idx - 1], maxOfA[idx - 1] - array[idx])
        maxOfAMinusB.append(currentMax)
    for idx in range(2, len(array)):
        currentMax = max(maxOfAMinusBPlusC[idx - 1], maxOfAMinusB[idx - 1] + array[idx])
        maxOfAMinusBPlusC.append(currentMax)

    for idx in range(3, len(array)):
        currentMax = max(maxOfAMinusBPlusCMinusD[idx - 1], maxOfAMinusBPlusC[idx - 1] - array[idx])
        maxOfAMinusBPlusCMinusD.append(currentMax)

    return maxOfAMinusBPlusCMinusD[len(maxOfAMinusBPlusCMinusD) - 1]
