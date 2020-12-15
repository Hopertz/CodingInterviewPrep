# Validate Subsequence
def validated_sub1(array, subsequence):
    # time O(n) space O(1)
    seq_id = 0
    for value in array:
        if value == subsequence[seq_id]:
            seq_id += 1

        if seq_id == len(subsequence):
            return True

    return False


def validated_sub2(array, subsequence):
    # time O(n) space O(1)
    arr_id = 0
    seq_id = 0
    while arr_id < len(array) and seq_id < len(subsequence):
        if array[arr_id] == subsequence[seq_id]:
            seq_id += 1
        arr_id += 1

    return len(subsequence) == seq_id


print(validated_sub1([1, 2, 3, 4, 5, 6, 7], [1, 4, 7]))
print(validated_sub2([1, 2, 3, 4, 5, 6, 7], [1, 4, 7]))
