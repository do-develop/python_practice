"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to
efficiently store and retrieve keys in a dataset of strings. There are various
applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class
"""

class TrieNode:
    def __init__(self):
        self.children = {}  #hash map
        self.endOfWord = False
        

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
      

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True



# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("word")
param_2 = obj.search("word")
param_3 = obj.startsWith("wo")
param_4 = obj.search("wo")
param_5 = obj.startsWith("te")

print(param_2, param_3, param_4, param_5, end=" ")
