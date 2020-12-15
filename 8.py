# PRODUCT SUM
def productSum(array, depth=1):
    # Write your code here.
    sumn = 0
    for elem in array:
        if isinstance(elem, list):
            sumn += productSum(elem, depth + 1)
        else:
            sumn += elem
    return depth * sumn




