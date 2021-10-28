"""
  Group Anagrams

  Write a function that takes in array of strings and groups anagrams together

  Anagrams are strings made up of exactly the same letters,where order doesn't matter.
  For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.

  Your function should return a list of anagram groups in no particular order.

  Sample Input
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

  Sample Output
     [["yo","oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]

"""
# SOLUTION 1

# O(w * n * log(n) time | O(n) space - where w is the number of words
# where n is the length of the longest word.
def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedword = "".join(sorted(word))
        if sortedword in anagrams:
            anagrams[sortedword].append(word)
        else:
            anagrams[sortedword] = [word]

    return list(anagrams.values())




