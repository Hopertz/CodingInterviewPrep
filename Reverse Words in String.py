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
     "best the is AlgoExpert"
"""


def reverseString(string):
    res = ''
    new = ''
    for indx in range(len(string) - 1, -1, -1):
        if string[indx] == ' ' or indx == 0:
            space = ' ' if not indx == 0 else ''
            begin = string[indx] if indx == 0 else ''
            word = ''
            for j in range(len(new) - 1, -1, -1):
                word += new[j]
            res += begin + word + space
            new = ''
            continue
        new += string[indx]
    return res




