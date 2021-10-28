"""
    Multi String Search
  Write a function that takes in a big string and an array of small strings, all of which are smaller in length than the big
  string. The function should return an array of booleans, where each boolean represents whether the small string at that
  index in the array of small strings is contained in the big string.
  Note that you can't use language-built-in string-matching methods.

  Sample Input #1
    bigString = "this is a big string"
    smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]

  Sample Output #1
       [true, false, true, true, false, true, false]

  Sample Input #2
     bigString = "abcdefghijklmnopqrstuvwxyz"
     smallStrings = ["abc", "mnopqr", "wyz", "no", "e", "tuuv"]

  Sample Output #2
     [true, true, false, true, true, false]

"""

# SOLUTION 1

# O(bns) time | O(n) space
def multiStringSearch(bigString, smallStrings):
    return [isInBigString(bigString, smallString) for smallString in smallStrings]


def isInBigString(bigString, smallString):
    for i in range(len(bigString)):
        if i + len(smallString) > len(bigString):
            break
        if isInBigStringHelper(bigString, smallString, i):
            return True
    return False


def isInBigStringHelper(bigString, smallString, startIdx):
    leftBigIdx = startIdx
    rightBigIdx = startIdx + len(smallString) - 1
    leftSmallIdx = 0
    rightSmallIdx = len(smallString) - 1
    while leftBigIdx <= rightBigIdx:
        if bigString[leftBigIdx] != smallString[leftSmallIdx] or bigString[rightBigIdx] != smallString[rightSmallIdx]:
            return False
        leftBigIdx += 1
        rightBigIdx -= 1
        leftSmallIdx += 1
        rightSmallIdx -= 1
    return True


# SOLUTION 2

# 0(b^2 + ns) time | 0(b^2 + n) space
def multiStringSearch(bigString, smallStrings):
    modifiedSuffixTrie = ModifiedSuffixTrie(bigString)
    return [modifiedSuffixTrie.contains(string) for string in smallStrings]


class ModifiedSuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.populateModifiedSuffixTrieFrom(string)

    def populateModifiedSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return True
