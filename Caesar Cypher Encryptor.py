"""
  Caesar Cypher Encryptor

  Give a non-empty string of lowercase letters and a non negative integer representing
  a key,write a function that returns a new string obtained by shifting every letter in
  the input string by k positions in the alphabet,where k is the key.

  Note that the letters should "wrap" around the alphabet,in other words,the letter z
  shifted by one returns the letter a.

  Sample Input
    string = 'xyz'
    key = 2

  Sample Output
     "zab"

"""


# Running time O(n)| space 0(n)
def caesarCipherEncryptor1(string, key):
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    key = key % 26
    newString = []
    for letter in string:
        newlettercode = (ord(letter) - 97) + key
        idx = newlettercode % 26
        newString.append(alphabets[idx])

    return ''.join(newString)


# Running time O(n)| space 0(n)
def caesarCipherEncryptor2(string, key):
    newString = []
    key = key % 26
    for letter in string:
        newLettercode = ord(letter) + key
        if newLettercode <= 122:
            newString.append(chr(newLettercode))
        else:
            newString.append(chr(96 + newLettercode % 122))

    return ''.join(newString)

