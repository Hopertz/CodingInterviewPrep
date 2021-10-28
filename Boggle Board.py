"""
   Boggle Board
  You're given a two-dimensional array (a matrix) of potentially unequal height and width containing letters, this matrix represents a
  boggle board. You're also given a list of words.

  Write a function that returns an array of all the words contained in the boggle board. The final words don't need to be in any particular
  order.
  A word is constructed in the boggle board by connecting adjacent (horizontally, vertically, or diagonally) letters, without using any single
  letter at a given position more than once; while a word can of course have repeated letters, those repeated letters must come from
  different positions in the boggle board in order for the word to be contained in the board. Note that two or more words are allowed to
  overlap and use the same letters in the boggle board.

  Sample Input
    board  = [
       ["t", "h", "i", "s", "i", "s", "a"],
       ["s", "i", "m", "p", "l", "e", "x"],
       ["b", "x", "x", "x", "x", "e", "b"],
       ["x", "o", "g", "g", "l", "x", "o"],
       ["x", "x", "x", "D", "T", "r", "a"],
       ["R", "E", "P", "E", "A", "d", "x"],
       ["x", "x", "x", "x", "x", "x", "x"],
       ["N", "0", "T", "R", "E", "-", "P"],
       ["x", "x", "D", "E", "T", "A", "E"],
       ],
   words = [
      "this", "is", "not", "a", "simple", "boggle",
      "board", "test", "REPEATED", "NOTRE-PEATED",
   ]
   
  Sample Output
   ["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]
   // The words could be ordered differently.

"""

# SOLUTION 1

# O(nm*8^S + ws) time | O(nm + ws) space
def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    visited = [[False for letter in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root, visited, finalWords)
    return list(finalWords.keys())


def explore(i, j, board, trieNode, visited, finalWords):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in trieNode:
        return
    visited[i][j] = True
    trieNode = trieNode[letter]
    if "*" in trieNode:
        finalWords[trieNode["*"]] = True
    neighbors = getNeighbors(i, j, board)
    for neighbor in neighbors:
        explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords)
    visited[i][j] = False


def getNeighbors(i, j, board):
    neighbors = []
    if i > 0 and j > 0:
        neighbors.append([i - 1, j - 1])
    if i > 0 and j < len(board[0]) - 1:
        neighbors.append([i - 1, j + 1])
    if i < len(board) - 1 and j < len(board[0]) - 1:
        neighbors.append([i + 1, j + 1])
    if i < len(board) - 1 and j > 0:
        neighbors.append([i + 1, j - 1])
    if i > 0:
        neighbors.append([i - 1, j])
    if i < len(board) - 1:
        neighbors.append([i + 1, j])
    if j > 0:
        neighbors.append([i, j - 1])
    if j < len(board[0]) - 1:
        neighbors.append([i, j + 1])
    return neighbors


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word
