class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Contains all the words present
        found = []
        visit = set()

        # Creating prefix tree of words
        trie = Trie()
        for word in words:
            trie.addWord(word)

        def dfs(i, j, cur, prefix):  
            # Base case (failure)
            if i not in range(len(board)) or j not in range(len(board[0])) or not cur or (i, j) in visit:
                return
                
            # Base case (success)
            if cur.endWord and (prefix not in found):
                found.append(prefix)
            
            # Recursive case
            visit.add((i, j))

            neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in neighbors:
                row, col = i + dr, j + dc

                # Calling DFS if char matches
                if row in range(len(board)) and col in range(len(board[0])) and (board[row][col] in cur.children):
                    boardChar = board[row][col]
                    dfs(row, col, cur.children[boardChar], prefix + boardChar)

            visit.remove((i, j))
        
        # Making DFS calls for each starting cell
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.root.children: 
                    dfs(i, j, trie.root.children[board[i][j]], "".join(board[i][j]))

        return found