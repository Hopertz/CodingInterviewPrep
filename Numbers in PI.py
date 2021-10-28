"""
   Numbers In Pi  ☆
  Given a string representation of the first n digits of Pi and a list of positive integers (all in string format),
  write a function that returns the smallest
  number of spaces that can be added to the n digits of Pi such that all resulting numbers are found in the list of integers.
  Not e that a single number can appear multiple times in the resulting numbers. For example, if Pi is "3141" and the numbers are
  ["1", "3", "4"] , the number "1" is allowed to appear twice in the list of resulting numbers after three spaces are added:
  "3 | 1 | 4 | 1"
  If no number of spaces to be added exists such that all resulting numbers are found in the list of integers, the function should return -1.

  Sample Input
       pi = "3141592653589793238462643383279",
       numbers = ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]

  Sample Output
    2 // "314159265 | 35897932384626433832 | 79"

"""
# SOLUTION 1

# O(n^3 + m) time | O(n + m) space - where n is the number of digits in Pi and m is the number of favorite numbers
def numbersInPi(pi, numbers):
    numbersTable = {number: True for number in numbers}
    minSpaces = getMinSpaces (pi, numbersTable, {}, 0)
    return -1 if minSpaces == float("inf") else minSpaces

def getMinSpaces(pi, numbersTable, cache, idx):
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces = float("inf")
    for i in range(idx, len(pi)):
        prefix = pi[idx : i + 1]
        if prefix in numbersTable:
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    cache[idx] = minSpaces
    return cache[idx]

# SOLUTION 2

# O(n^3 + m) time | O(n + m) space where n is the number of digits in Pi and m is the number of favorite numbers
def numbersInPi(pi, numbers):
    numbersTable = {number: True for number in numbers}
    cache = {}
    for i in reversed(range(len(pi))):
        getMinSpaces(pi, numbersTable, cache, i)
    return -1 if cache[0] == float("inf") else cache[0]

def getMinSpaces(pi, numbersTable, cache, idx):
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces = float("inf")
    for i in range(idx, len(pi)):
        prefix = pi[idx : i + 1]
        if prefix in numbersTable:
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    cache[idx] = minSpaces
    return cache[idx]

