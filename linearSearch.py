'''
This is the traditional technique for searching an element in a collection of elements. 
In this type of search, all the elements of the list are traversed one by one to find if the element is 
present in the list or not

Linear search algorithm is straightforward and has O(n) of complexity

Algorithm:

= Start from the leftmost element of given arr[] and one by one compare element x with each element of arr[]
= If x matches with any of the element, return the index value.
= If x doesn’t match with any of elements in arr[] , return -1 or element not found.

By Innocent Suta
'''

def LinearSearch(elements, target):
    
    for i in range(len(elements)):
        
        if elements[i] == target:
            
            return i
        
    return -1


elements = ['i', 'n', 'n', 'o', 'c', 'e', 'n', 't', 's', 'u', 't', 't', 'a']

target = 'e'

print("An item is found at index " + str(LinearSearch(elements, target)))
