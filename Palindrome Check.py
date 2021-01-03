# Palindrome Check

# Running time O(n) space 0(1)
def isPalindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


print(ord('x'), ord('z'))
