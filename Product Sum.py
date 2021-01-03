# PRODUCT SUM

# Running time O(n) space 0(d) where n is total number of elements
# including sub-elements, and d is the greatest depth of special arrays in the array.
def productSum(array, depth=1):
    # Write your code here.
    sumn = 0
    for elem in array:
        if isinstance(elem, list):
            sumn += productSum(elem, depth + 1)
        else:
            sumn += elem
    return depth * sumn




