"""
  Generate Document
  You're given a string of available characters and a string representing a document
  that you need to generate.Write a function that determines if you can generate the
  document using the available charcters.If you can generate the document,your function
  should return true; otherwise,it should return false.

  You're only able to generate the document if the frequency of unique characters in the
  characters string is greater than or equal to the frequency of unique characters in the
  document string.For example , if you're given characters = "abcabc" and
  document = "aabbccc" you cannot generate the document because you're missing one c.

  The document that you need to create may contain any characters, including special
  characters, capital letters, numbers and spaces.

  Sample Input
    characters = "Bste!hetsi ogEAxpelrt x "
    document = "AlgoExpert is the Best!"

  Sample Output
    True
"""
# SOLUTION 1

# O(n + m) time | O(c) space - where n is the number of characters,m is the length of the
# document , and c is the number of unique characters in the string.

def generateDocument(characters, document):
    characterCounts = {}

    for character in characters:
        if character not in characterCounts:
            characterCounts[character] = 0
        characterCounts[character] += 1
    for character in document:
        if character not in characterCounts or characterCounts[character] == 0:
            return False

        characterCounts[character] -= 1

    return True

# SOLUTION 2

# O(m * (n + m)) time | O(1) space - where n is the number of characters,m is the length of the
# document.
def generateDocument(characters, document):
    for character in document:
        documentFrequency = countCharacterFrequency(character, document)
        characterFrequency = countCharacterFrequency(character, characters)
        if documentFrequency > characterFrequency:
            return False

    return True

def countCharacterFrequency(character, target):
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1

    return frequency

# SOLUTION 3

# O(c * (n + m)) time | O(c) space - where n is the number of characters,m is the length of the
# document , and c is the number of unique characters in the string.
def generateDocument(characters, document):
    alreadyCounted = set()
    for character in document:
        if character in alreadyCounted:
            continue

        documentFrequency = countCharacterFrequency(character, document)
        characterFrequency = countCharacterFrequency(character, characters)
        if documentFrequency > characterFrequency:
            return False

        alreadyCounted.add(character)

    return True

def countCharacterFrequency(character, target):
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1

    return frequency

