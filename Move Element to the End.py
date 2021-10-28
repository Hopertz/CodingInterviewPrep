"""
   Move Element to the End

   You're given an array of integers and an integer.Write a function that moves all
   instances of that integer in the array to the end of the array and returns the array.

   The function should perform this place (i.e it should mutate the input array) and
   doesn't need to maintain the order of the other integers.

   Sample Input
      array = [2, 1, 2 ,2 , 2, 3, 4, 2]
      toMove = 2

   Sample Output
       [1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1,3, and 4 could be ordered differently.


"""
# SOLUTION 1

# O(n) time | O(1) space where n is the length of array.
def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
           array[i], array[j] = array[j], array[i]
        i += 1
    return array


# SOLUTION 2

# O(n^2) time | O(1) space where n is the length of array.
def moveElementToEnd(array, toMove):
    for i in array:
        if i == toMove:
            array.remove(i)
            array.append(i)
    return array





