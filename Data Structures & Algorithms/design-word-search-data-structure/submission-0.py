class TrieNode:
    # Data structure in which the node contains references to all it's children nodes 
    # We can use a hashmap for O(1) look up
    def __init__(self):
        self.children = {}
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        # Inserting every character in the char in Trie structure
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        # Marking end of word
        cur.endWord = True

    def search(self, word: str, cur=None) -> bool:
        if not cur:
            cur = self.root

        for i in range(len(word)):
            if word[i] in cur.children: # standard case
                cur = cur.children[word[i]]
            elif word[i] == ".": # wild card case
                # Calling search on every possible wild card value
                for childNode in cur.children.values():
                    if self.search(word[i+1:], childNode):
                        return True

                return False
            else: # char does not match
                return False
        
        # Only return True if it is actually end of a word
        return cur.endWord
