""""
    Find Three Largest Numbers

    Write a function that takes in an array of at least three integers and ,without
    sorting the input array,returns a sorted array of the three largest integers in
    the input array.

    The function should return duplicate integers if necessary; for example, it should
    return [ 10, 10, 12] for an input array of [10, 5, 9, 10, 12]

    Sample Input
       array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

    Sample Output
       [18, 141, 541]
"""


# Running time O(n^2) because of list.remove() space O(1)
def findThreeLargestNumbers(array):
    # Write your code here.
    answ = [None, None, None]
    for i in range(2, -1, -1):
        res = max(array)
        answ[i] = res
        array.remove(res)
    return answ


# Running time O(n) space O(1)
def findThreeLargestNumbers(array):
    res = [None, None, None]
    for elem in array:
        update(res, elem)
        print(res)

    return res


def update(res, elem):
    if res[2] is None or elem > res[2]:
        shiftupdate(res, elem, 2)
    elif res[1] is None or elem > res[1]:
        shiftupdate(res, elem, 1)
    elif res[0] is None or elem > res[0]:
        shiftupdate(res, elem, 0)


def shiftupdate(res, elem, indx):
    # eg res =[x,y,z] and updating z = num
    # res = [y,z,num]

    for i in range(indx + 1):
        if i == indx:
            res[i] = elem
        else:
            res[i] = res[i + 1]


"""
   Running the below function
   findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7])
  
   Finding three largest number is done like this  for the 2nd solution
    [None, None, 141]
    [None, 1, 141]
    [1, 17, 141]
    [1, 17, 141]
    [1, 17, 141]
    [1, 17, 141]
    [17, 18, 141]
    [18, 141, 541]
    [18, 141, 541]
    [18, 141, 541]
    [18, 141, 541]
 
"""

