"""
  Three Number Sort

  You're given an array of integers and another array of three distinct
  integers.The first array is guaranteed to only contain integers that are in
  the second array,and the second array represents a desired order for the
  integers in the first array.For example, a second array of [x, y, z] represents
  a desired order of  [x, x, ..., x, y, y, ..., y, z, z, ..., z] in the first array.

  Write a function that sorts the first array according to the desired order
  in the second array.

  The function should perform this in place (i.e it should mutate the input array),
  and that the first array won't necessarily contain all three integers found in the
  second array-it might only contain one or two.

  Sample Input
     array = [1, 0, 0, -1, -1, 0, 1, 1]
     order = [0, 1, -1]

  Sample Output
     [0, 0, 0, 1, 1, 1, -1, -1]

"""
# SOLUTION 1

# time O(n) | space O(1) where n is the length of array.
def threeNumberSort(array, order):
    position = 0
    for i in range(len(order)):
        for j in range(len(array)):
            if order[i] == array[j]:
                array[position], array[j] = array[j], array[position]
                position += 1

    return array


