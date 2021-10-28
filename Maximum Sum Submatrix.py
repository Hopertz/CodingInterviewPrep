"""
     Maximum Sum Submatrix  *
   You're given a two-dimensional array la matrix) of potentially unequal height and width that's filled with integers.
   You're also given a positive integer size.Write a function that returns the maximum sum that can be
   generated from a submatrix with dimensions size = size.
   For example, consider the following matrix
       [
          [2, 4]
          [5, 6],
          [-3, 2]
       ]
   If size = 2, then the 2x2 submatrices to consider are:
         [2, 4]
         [5, 6]
   The sum of the elements in the first submatrix is 17 and the sum of the elements in the second submatrix is 18.
   In this example, your function should return 17 -
   Note: size will always be at least 1. and the dimensions of the input matrix will always be at least size * size.

   Sample Input
     matrix =
     [
        [5, 3, -1, 5],
        [-7, 3, 7, 4],
        [12, 8, e, e],
        [1, -8, -8, 2],
     ]
     size = 2

   Sample Output
       18
     //
     // [. ,. ,. ,. ],
     // [. , 3, 7,. ],
     // [., 8, 0 , .],
     // [., ., . , .]
     // ]

"""
# SOLUTION 1

# O(w * h) time | (w h) space - where w is
# the width of the matrix and h is the height
def maximumSumSubmatrix(matrix, size):
    sums = createSumMatrix(matrix)
    maxSubMatrixSum = float("-inf")

    for row in range(size - 1, len(matrix)):
        for col in range(size - 1, len(matrix[row])):
            total = sums[row][col]
            touchesTopBorder = row - size < 0
            if not touchesTopBorder:
                total -= sums[row - size][col]

            touchesLeftBorder = col - size < 0
            if not touchesLeftBorder:
                total -= sums[row][col - size]
            touchesTopOrLeftBorder = touchesTopBorder or touchesLeftBorder
            if not touchesTopOrLeftBorder:
                total += sums[row - size][col - size]
            maxSubMatrixSum = max(maxSubMatrixSum, total)

    return maxSubMatrixSum
def createSumMatrix(matrix):
    sums = [ [0 for _ in range(len(matrix[row]))] for row in range(len(matrix))]
    sums[0][0] = matrix[0][0]

    # Fill the first row.
    for idx in range(1, len(matrix[0])):
        sums[0][idx] = sums[0][idx - 1] + matrix[0][idx]

    # Fill the first column.
    for idx in range(1, len(matrix)):
        sums[idx][0] = sums[idx - 1][0] + matrix[idx][0]

    # Fill the rest of the matrix.
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
             sums[row][col] = sums[row - 1][col] + sums[row][col - 1] - sums[row -1][col - 1] + matrix[row][col]
    return sums
