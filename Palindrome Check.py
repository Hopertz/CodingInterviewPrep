"""
   Palindrome Check

   Write a function that takes in a non-empty string and tha returns a boolean representing
   whether the string is a palindrome.

   A palindrome is defined as a string that's written the same forward and backward.Note
   that single-character strings are palindromes.

   Sample Input
     string = 'abcdcba'

   Sample Output
      true // it's written the same forward and backward


"""
# SOLUTION 1

# Running time O(n) | space 0(1)
def isPalindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

# SOLUTION 2

# Running time O(n^2) | space 0(1)
def isPalindrome(string):
    reversedstring = ""
    for i in reversed(range(len(string))):
        reversedstring += string[i]
    return string == reversedstring

# SOLUTION 3

# Running time O(n) | space 0(n)
def isPalindrome(string):
    reversedchars = []
    for i in reversed(range(len(string))):
        reversedchars.append(string[i])
    return string == "".join(reversedchars)

# SOLUTION 4

# Running time O(n) | space 0(n)
def isPalindrome(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i+1)

# SOLUTION 5

# Below we are using Tail Recursion
# Running time O(n) | space 0(1)
def isPalindrome(string, i=0):
    j = len(string) - 1 - i
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindrome(string, i+1)


