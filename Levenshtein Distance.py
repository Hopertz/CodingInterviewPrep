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
# SOLUTION 1

# O(n*m) time | O(n) space where n and m are the strings lengths.
def levenshteinDistance(str1, str2):
    if str1 == '' or str2 == '':
        return len(str1) or len(str2)

    dp = [[float('inf') for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    dp[0][0] = 0
    for i in range(1, len(dp)):
        dp[i][0] = i
    for j in range(1, len(dp[0])):
        dp[0][j] = j

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

    return dp[-1][-1]


# SOLUTION 2

# O(n*m) time | O(n) space where n and m are the strings lengths.
def levenshteinDistance(str1, str2):
    dp = [[x for x in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        dp[i][0] = dp[i - 1][0] + 1
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[-1][-1]


