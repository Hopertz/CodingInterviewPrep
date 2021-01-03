# Caesar Cypher Encryptor

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

new ='wer'
print(new.index('w'))
print(len(new)-1)
print(f'9a')