"""
  Levenshtein Distance

  Write a function that takes in two strings and returns the minimum number of
  edit operations that need to be performed on the first string to obtain the
  second string.

  There are three edit operations: Insertion of a character, deletion of a
  character, and substitution of a character for another.

  Sample Input
     str1 = "abc"
     str2 = "yabd"

  Sample Output
     2 // insert "y"; substitute "c" for "d"


"""


def levenshteinDistance(str1, str2):
    c = 0
    for i in range(len(str2)):
         if not str1[0:i] == str2[0:i]:
            str1 = str1[0:i] + str2[i] + str1[i:]
            c += 1
    return c



