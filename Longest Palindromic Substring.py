"""
  Longest Palindromic Substring

  Write a function that,given a string returns its longest palindromic substring.

  A palindrome is defined as a string thats written the same forward and backward.Note
  that single-character strings are palindromes.

  You can assume that there will only be one longest palindromic substring.

  Sample Input
    string = "abaxyzzyxf"

  Sample Output
    "xyzzyz"
"""

# SOLUTION 1

# O(n^3) time | O(n) space
def longestPalindromicSubstring(string):
    longest = ''
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i: j + 1]
            if len(substring) > len(longest) and isPalindrome(substring):
                longest = substring
    return longest

def isPalindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

