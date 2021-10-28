"""
    Longest Substring Without Duplication *
  Write a function that takes in a string and returns its longest substring without duplicate characters.
  You can assume that there will only be one longest substring without duplication.

  Sample Input
      string = "clementisacap"
  Sample Output
     "mentisac"

"""
# SOLUTION 1

# O(n) time | 0(min(n, a)) space
def longestSubstringWithoutDuplication(string):
    lastSeen = {}
    longest = [0, 1]
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            startIdx = max(startIdx, lastSeen[char] + 1)
        if longest[1] - longest[0] < i + 1 - startIdx:
            longest = [startIdx, i + 1]
        lastSeen[char] = i
    return string[longest[0] : longest[1]]

