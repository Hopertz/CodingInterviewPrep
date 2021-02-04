# Move Element to the End

# O(n) time | O(1) space where n is the length of array.
def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i<j:
        while i<j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
           array[i], array[j] = array[j], array[i]
        i += 1
    return array

# O(n^2) time | O(1) space where n is the length of array.
def moveElementToEnd(array, toMove):
    # Write your code here.
    for i in array:
        print(array)
        if i == toMove:
            array.remove(i)
            array.append(i)
    return array


'''
input
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
output
[1, 3, 4, 2, 2, 2, 2, 2]
print(moveElementToEnd(array, toMove))
'''



