"""
  Four Number Sum
  Write a function that takes in a non-empty array of distinct integers and an integer representing
  a target  sum.The function should find all quadruplets in the array that sum up to the target sum
  and return a two dimensional array of ll these quadruplets in no particular order.

  If no four numbers sum up to the target sum,the function should return an empty array.

  Sample Input
     array = [7, 6, 4, -1, 1, 2]
     targetSum = 16

  Sample Output
     [[7,6,4,-1], [7,6,1,2]] //the quadruplets could be ordered differently
"""

le = 18
w = 6
c = '.|.'
lw = (le-3)//2

for i in range(w//2):
    print(('-'*(lw-(i*3))+(c*i)+c+(c*i)+('-'*(lw-(i*3)))))
print('WELCOME'.center(le, '-'))
for i in range(w//2-1, -1, -1):
    print(('-'*(lw-(i*3))+(c*i)+c+(c*i)+('-'*(lw-(i*3)))))
