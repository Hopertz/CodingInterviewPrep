"""
  First Non-Repeating Character

  Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the
  string's first non-repeating character.

  The first non-repeating character is the first character in a string that occurs only once.

  If the input string doesn't have any non-repeating characters your function should return -1.

  Sample input
    string = "abcdaf"

  Sample Output
     1  // The first non-repeating character is 'b' and is found at index 1.

"""


# O(n) time | O(1) space - where n is the length of the input string
# The constant space is because the input string only has lowercase
# English-alphabet letters; thus ,our hash table will never have more
# than 26 character frequencies.
def firstNonRepeatingCharacter(string):
    letters = countString(string)

    for indx, letter in enumerate(string):
        if letters[letter] == 1:
            return indx

        return -1


def countString(string):
    letters = {}
    for indx, letter in enumerate(string):
        value = letters.setdefault(letter, 0)
        letters[letter] = value + 1
    return letters


# O(n^2) time | O(1) space - where n is the length of the input string
def firstNonRepeatingCharacter(string):
    for idx in range(len(string)):
        foundDuplicate = False
        for idx2 in range(len(string)):
            if string[idx] == string[idx2] and idx != idx2:
                foundDuplicate = True
        if not foundDuplicate:
            return idx
    return -1
