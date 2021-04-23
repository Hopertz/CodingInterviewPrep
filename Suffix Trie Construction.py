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