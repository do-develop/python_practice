class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        dp = {len(s): 0}
        trie = Trie(dictionary).root

        def dfs(i):
            if i in dp:
                return dp[i]

            # Skip current character
            res = 1 + dfs(i + 1)
            curr = trie

            # Try to match using Trie
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.is_word:
                    res = min(res, dfs(j + 1))
            
            dp[i] = res
            return res

        return dfs(0)
