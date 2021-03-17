"""
  Write a function that takes in an array of unique integers and returns an array
  of all permutations of those integers in no particular order.

  If the input array is empty,the function should return an empty array

  Sample Input
    array = [1, 2, 3]

  Sample Output
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    
"""
# Upper Bound: O(n^2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space

def getPermutation(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPermutation = currentPermutation + [array[i]]
            permutationsHelper(newArray, newPermutation, permutations)