"""
  Knuth—Morris—Pratt Algorithm
  Write a function that takes in two strings and checks if the first string contains the second one using the
  Knuth—Morris—Pratt algorithm. The function should return a boolean.
  If you're unfamiliar with the Knuth—Morris—Pratt Algorithm, we recommend watching the Conceptual Overview section
  of this question's video explanation before starting to code.

  Sample Input
     string = "aefoaefcdaefcdaed"
     substring = "aefcdaed"

  Sample Output
     true

"""

# SOLUTION 1

# O(n + m) time | 0(m) space
def knuthMorrisPrattAlgorithm(string, substring):
    pattern = buildPattern(substring)
    return doesMatch(string, substring, pattern)

def buildPattern(substring):
    pattern = [-1 for i in substring]
    j = 0
    i = 1
    while i < len(substring):
        if substring[i] == substring[j]:
            pattern[i] =j
            i += 1
            j += 1
        elif j>0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return pattern

def doesMatch(string, substring, pattern):
    i = 0
    j = 0
    while i + len(substring) - j <= len(string):
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                return True
            i += 1
            j += 1
        elif j > 0:
             j = pattern[j - 1] + 1

        else:
            i += 1
    return False
