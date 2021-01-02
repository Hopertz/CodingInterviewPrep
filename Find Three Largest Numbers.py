# THREE LARGEST NUMBERS

# Solution One
# Running time O(n^2) because of list.remove() space O(1)
def findThreeLargestNumbers1(array):
    # Write your code here.
    answ = [None, None, None]
    for i in range(2, -1, -1):
        res = finder(array)
        answ[i] = res
        array.remove(res)
    return answ


def finder(array):
    num = array[0]
    for elem in array:
        if elem > num:
            num = elem
    return num


# Solution Two
# Running time O(n) space O(1)
def findThreeLargestNumbers2(array):
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


print(findThreeLargestNumbers1([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
print(findThreeLargestNumbers2([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
