# THREE NUMBER SUM

# time O(n^3) | space O(1)
def threeNumberSum(array, targetSum):
    array.sort()

    triplets = []
    for i in range(len(array) - 2):
        first_no = array[i]
        for j in range(i + 1, len(array) - 1):
            second_no = array[j]
            for k in range(j + 1, len(array)):
                third_no = array[k]
                if first_no + second_no + third_no == targetSum:
                    triplets.append([first_no, second_no, third_no])

    return triplets


# time O(n^2)  space O(n)
def threeNumberSum2(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            if array[i] + array[left] + array[right] == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif array[i] + array[left] + array[right] < targetSum:
                left += 1
            elif array[i] + array[left] + array[right] > targetSum:
                right -= 1
    return triplets
