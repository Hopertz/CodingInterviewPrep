"""
   Suffix Trie Construction

   Write a SuffixTrie class for a Suffix-Trie-like data structure. The class should have a root property set to be the
   root node of the trie and should support:
      • Creating the trie from a string this will be done by calling the populateSuffixTrieFrom method upon class
        instantiation, which should populate the root of the class.
      • Searching for strings in the trie.

   Note that every string added to the trie should end with the special endSymbol character: "*"
   If you're unfamiliar with Suffix Tries, we recommend watching the Conceptual Overview section of this question's
   video explanation before starting to code.

   Sample Input (for creation)
       string = "babc"

   Sample Output (for creation)
       The structure below is the root of the trie.
       {
       "C": {"*": true},
       "b": {
       "c": {"*": true},
       "a": {"b": {"c": {"*": true}}},
       },
       "a": {"b": {"c": {"*": true}}},
       }

   Sample Input (for searching in the suffix trie above)
      string = "abc"

   Sample Output (for searching in the suffix trie above)
       true
   
"""
# SOLUTION 1

# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)
    
     # O(n^2) time | O(n^2) space
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
             self.insertSubstringStartingAt(i,string)

    def insertSubstringStartingAt(self, i, string):
         node = self.root
         for j in range(i, len(string)):
             letter = string[j]
             if letter not in node:
                node[letter] = {}
             node = node[letter]
              node[self.endSymbol] = True

    # O(m) time | O(1) space
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
               return False
            node = node[letter]
        return self.endSymbol in node
        
