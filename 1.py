# Two number sum
def two_sum1(array, target_sum):
    # time O(n^2)  space O(1)
    for i in range(len(array) - 1):
        first_no = array[i]
        for j in range(i + 1, len(array)):
            second_no = array[j]
            if first_no + second_no == target_sum:
                return [first_no, second_no]
    return []


def two_sum2(array, target_sum):
    # time O(n)  space O(n)
    nums = {}
    for num in array:
        potential_num = target_sum - num
        if potential_num in nums:
            return [potential_num, num]
        else:
            nums[num] = True
    return []


def two_sum3(array, target_sum):
    # time O(nlog(n))  space O(1)
    left = 0
    right = len(array) - 1
    array.sort()
    while left < right:
        if array[left] + array[right] == target_sum:
            return [array[left], array[right]]

        elif array[left] + array[right] < target_sum:
            left += 1

        else:
            right += 1
    return []


print(two_sum1([3, 6, 5, 9, 2, 7], 14))
print(two_sum2([3, 6, 5, 9, 2, 7], 14))
print(two_sum3([3, 6, 5, 9, 2, 7], 14))
