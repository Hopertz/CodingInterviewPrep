"""
        Longest Balanced Substring →
   Write a function that takes in a string made up of parentheses ( ( and ) ). The function should return an integer
   representing the length of the
   longest balanced substring with regards to parentheses.
   A string is said to be balanced if it has as many opening parentheses as it has closing parentheses and if no
   parenthesis is unmatched. Note that
   an opening parenthesis can't match a closing parenthesis that comes before it, and similarly, a closing parenthesis
   can't match an opening
   parenthesis that comes after it.

   Sample Input
      string = "(())"

   Sample Output
     4 // The longest balanced substring is "(0)".


"""

# SOLUTION 1

# O(n^3) time | O(n) space - where n is the length of the input string
def longestBalancedSubstring(string):
    maxLength = 0
    for i in range(len(string)):
        for j in range(i + 2, len(string) + 1, 2):
            if isBalanced(string[i:j]):
                currentLength = j - i
                maxLength = max(maxLength, currentLength)

    return maxLength


def isBalanced(string):
    openParensStack = []
    for char in string:
        if char == "(":
            openParensStack.append("(")
        elif len(openParensStack) > 0:
            openParensStack.pop()
        else:
            return False
    return len(openParensStack) == 0


# SOLUTION 2

# O(n) time | O(n) space - where n is the length of the input string
def longestBalancedSubstring(string):
    maxlength = 0
    idxStack = []
    idxStack.append(-1)
    for i in range(len(string)):
        if string[i] == "(":
            idxStack.append(i)
        else:
            idxStack.pop()
            if len(idxStack) == 0:
                idxStack.append(i)
            else:
                balancedSubstringStartIdx = idxStack[len(idxStack) - 1]
                currentLength = i - balancedSubstringStartIdx
                maxlength = max(maxlength, currentLength)

    return maxlength


# SOLUTION 3

# O(n) time | 0(1) space - where n is the length of the input string
def longestBalancedSubstring(string):
    maxlength = 0
    openingCount = 0
    closingCount = 0

    for char in string:
        if char == "(":
            openingCount += 1
        else:
            closingCount += 1

        if openingCount == closingCount:
            maxlength = max(maxlength, closingCount * 2)
        elif closingCount > openingCount:
            openingCount = 0
            closingCount = 0
    openingCount = 0
    closingCount = 0
    for i in reversed(range(len(string))):
        char = string[i]
        if char == "(":
            openingCount += 1
        else:
            closingCount += 1

        if openingCount == closingCount:
            maxlength = max(maxlength, openingCount * 2)
        elif openingCount > closingCount:
            openingCount = 0
            closingCount = 0

    return maxlength


# SOLUTION 4

# O(n) time | 0(1) space - where n is the length of the input string
def longestBalancedSubstring(string):
    return max(
        getLongestBalancedInDirection(string, True),
        getLongestBalancedInDirection(string, False),
    )


def getLongestBalancedInDirection(string, leftToRight):
    openingParens = "(" if leftToRight else ")"
    startIdx = 0 if leftToRight else len(string) - 1
    step = 1 if leftToRight else -1

    maxlength = 0
    openingCount = 0
    closingCount = 0

    idx = startIdx

    while 0 <= idx < len(string):
        char = string[idx]

        if char == openingParens:
            openingCount += 1
        else:
            closingCount += 1

        if openingCount == closingCount:
            maxlength = max(maxlength, closingCount * 2)
        elif closingCount > openingCount:
            openingCount = 0
            closingCount = 0

        idx += step
    return maxlength
