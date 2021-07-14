"""
   Minimum Passes Of Matrix.py

   Write a function that takes in an integer matrix of potentially unequal height and width and returns the minimum number of passes required to convert
   all negative integers in the matrix to positive integers.A negative integer in the matrix can only be converted to a positive integer if one or more 
   of its adjacent elements is positive. An adjacent element is an element that is to the left, to the right, above, or below the current element in the 
   matrix. Converting a negative to a positive simply involves multiplying it by —1 .

   Note that the 0 value is neither positive nor negative, meaning that a 0 can't convert an adjacent negative to a positive.A single pass through the matrix 
   involves converting all the negative integers that can be converted at a particular point in time. For example, consider the following input matrix:

      [ 
        [ 0,-2, -1],
        [-5, 2,  0],
        [-6,-2,  0],
      ]

   After a first pass, only 3 values can be converted to positives:
   
      [ 
        [ 0, 2, -1],
        [ 5, 2,  0],
        [-6, 2,  0],
      ]
      
   After a second pass, the remaining negative values can all be converted to positives:
       [ 
        [ 0, 2, 1],
        [ 5, 2, 0],
        [ 6, 2, 0],
      ]


   Note that the input matrix will always contain at least one element. If the negative integers in the input matrix can't all be
   converted to positives, regardless of how many passes are run, your function should return —1 .

   Sample Input

     matrix = [
       [0,-1,-3, 2, 0],
       [1,-2,-5,-1,-3],
       [3, 0, 0,-4,-1]
     ]

   Sample Output
      3
      
"""







