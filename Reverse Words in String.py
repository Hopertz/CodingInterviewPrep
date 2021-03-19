"""
  Reverse Words in String

  Write a function that takes in a string of words separated by one or more
  whitespaces and returns a string that has these words in reverse order.
  For example,given the string "tim is great", your function should return
  "great is tim"

  For this problem, a word can contain special characters,punctuation, and numbers.
  the words in the string will be separated by one or more whitespaces, amd the
  reversed string must contain the same whitespaces as the original string.For example,
  given the string "whitespaces 4" you would be expected to return "4 whitespaces".

  Note that you're not allowed to use any built-in split or reverse methods/functions,
  you are allowed to use a built-in join method/function.

  Also note that thr input string isn't guaranteed to always contain words.

  Sample Input
    string = "AlgoExperts is the best!"

  Sample Output
     "best! the is AlgoExperts"
"""


# time O(n*w) | space O(1) n is the length of string.
# w is the length of new word formed.
def reverseWordsInString(string):
    result = ''
    newWord = ''
    for indx in range(len(string) - 1, -1, -1):
        if string[indx] == ' ' or indx == 0:
            space = ' ' if not indx == 0 else ''
            begin = string[indx] if indx == 0 else ''
            arrangeWord = ''
            for j in range(len(newWord) - 1, -1, -1):
                arrangeWord += newWord[j]
            result += begin + arrangeWord + space
            newWord = ''
            continue
        newWord += string[indx]
    return result


# time O(n) | space O(n) where n is the length of string.
def reverseWordsInString(string):
    words = []
    startofWord = 0
    for idx in range(len(string)):
        character = string[idx]

        if character == " ":
            words.append(string[startofWord:idx])
            startofWord = idx
        elif string[startofWord] == " ":
            words.append(" ")
            startofWord = idx

    words.append(string[startofWord:])

    reverseList(words)
    return "".join(words)


def reverseList(list):
    start, end = 0, len(list) - 1
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1


# time O(n) | space O(n) where n is the length of string.
def reverseWordsInString(string):
    characters = [char for char in string]
    reverseListRange(characters, 0, len(characters) - 1)

    startofWord = 0
    while startofWord < len(characters):
        endofWord = startofWord
        while endofWord < len(characters) and characters[endofWord] != " ":
            endofWord += 1

        reverseListRange(characters, startofWord, endofWord - 1)
        startofWord = endofWord + 1

    return "".join(characters)


def reverseListRange(list, start, end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1
