"""
   Interweaving Strings ☆
   Write a function that takes in three strings and returns a boolean representing whether the third string can be formed by interweaving
   the first two strings.
   To interweave strings means to merge them by alternating their letters without any specific pattern. For instance, the strings "abc"
   and "123" can be interwoven as "a1b2c3" , as "abc123" , and as "ab1c23" (this list is nonexhaustive).
   Letters within a string must maintain their relative ordering in the interwoven string.

   Sample Input
      one = "algoexpert"
      two = "your-dream-job"
      three = "your-algodream-expertjob"

   Sample Output
     true

"""

# SOLUTION 1

# 0(2^(n + m)) time | O(n + m) space where n is the length
# of the first string and m is the length of the second string
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False
    return areInterwoven(one, two, three, 0, 0)


def areInterwoven(one, two, three, i, j):
    k = i + j
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        if areInterwoven(one, two, three, i + 1, j):
            return True

    if j < len(two) and two[j] == three[k]:
        return areInterwoven(one, two, three, i, j + 1)

    return False


# SOLUTION 2

# O(nm) time | O(nm) space where n is the length of the
# first string and m is the length of the second string
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False

    cache = [[None for j in range(len(two) + 1)] for i in range(len(one) + 1)]
    return areInterwoven(one, two, three, 0, 0, cache)


def areInterwoven(one, two, three, i, j, cache):
    if cache[i][j] is not None:
        return cache[i][j]

    k = i + j
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        cache[i][j] = areInterwoven(one, two, three, i + 1, j, cache)
        if cache[i][j]:
            return True
    if j < len(two) and two[j] == three[k]:
        cache[i][j] = areInterwoven(one, two, three, i, j + 1, cache)
        return cache[i][j]

    cache[i][j] = False
    return False
