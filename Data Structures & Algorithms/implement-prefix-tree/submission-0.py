class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False # False by default

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endWord = True

    def search(self, word: str) -> bool: # Searching for the full word
        cur = self.root

        # Following dictionary for each char
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else: # Character not found in dictionary
                return False
        
        return cur.endWord # True if it is endWord
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False

        return True # Does not matter if end of word as long as prefix matches