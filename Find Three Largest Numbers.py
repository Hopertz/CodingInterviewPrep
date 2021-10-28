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

# SOLUTION 1

# Running time O(n^2) because of list.remove() space O(1)
def findThreeLargestNumbers(array):
    # Write your code here.
    answ = [None, None, None]
    for i in range(2, -1, -1):
        res = max(array)
        answ[i] = res
        array.remove(res)
    return answ


# SOLUTION 2

# Running time O(n) space O(1)
def findThreeLargestNumbers(array):
    res = [None, None, None]
    for elem in array:
        update(res, elem)
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


# SOLUTION 3

# Running time O(n) space O(1)
def findThreeLargestNumbers(array):
    answ = [None, None, None]
    for num in array:
        check(answ, num)
    return answ


def check(answ, num):
    # All values are None
    if answ[0] == answ[1] == answ[2] is None:
        answ[2] = num
    # Two values are None
    elif answ[0] == answ[1] is None:
        if num > answ[2]:
            answ[1], answ[2] = answ[2], num
        else:
            answ[1] = num
    # One Value is None
    elif answ[0] is None:
        if num > answ[2]:
            answ[0], answ[1], answ[2] = answ[1], answ[2], num
        elif num > answ[1]:
            answ[0], answ[1] = answ[1], num
        else:
            answ[0] = num

    # No Value is None
    else:
        if num > answ[2]:
            answ[0], answ[1], answ[2] = answ[1], answ[2], num
        elif num > answ[1]:
            answ[0], answ[1] = answ[1], num

        elif num > answ[0]:
            answ[0] = num
