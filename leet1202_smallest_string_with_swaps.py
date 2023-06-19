class Solution:
    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # union-find
        self.parent = list(range(len(s)))
        for a, b in pairs:
            self.union(a, b)
        
        # grouping
        grp = defaultdict(lambda: ([], []))
        for i, c in enumerate(s):
            parent = self.find(i)
            grp[parent][0].append(i)
            grp[parent][1].append(c)
        
        # sorting
        res = [''] * len(s)
        for idxes, chars in grp.values():
            idxes.sort()
            chars.sort()
            for c, i in zip(chars, idxes):
                res[i] = c
        
        return ''.join(res)

        
