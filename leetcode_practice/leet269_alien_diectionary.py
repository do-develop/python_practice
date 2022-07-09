"""
There is a new alien language which uses the latin alphabet. However, the
order among letters are unknown to you. You receive a list of words from the
dictionary, where words are sorted lexicographically by the rules of this new
language. Derive the order of letters in this language.
"""
from typing import List
# Solution - Topological sort

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        characters = set()
        for word in words:
            characters.update(word)

        adj = {c: [] for c in characters}
        indegree = {c: 0 for c in characters}

        for i in range(len(words) -1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    adj[words[i][j]].append(words[i+1][j])
                    indegree[words[i+1][j]] += 1

        # Topological sort
        queue = []
        result = []
        for c in characters:
            if indegree[c] == 0:
                queue.append(c)

        while queue:
            cur = queue.pop(0)
            result.append(cur)

            for a in adj[cur]:
                indegree[a] -= 1
                if indegree[a] == 0:
                    queue.append(a)

        return ''.join(result)
                


# TEST
if __name__ == '__main__':
    words = ["wrt","wrf","er","ett","rftt"]
    print(Solution().alienOrder(words))

            
            
