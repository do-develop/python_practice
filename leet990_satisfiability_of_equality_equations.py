class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # Union Find approach
        parent = {c: c for c in string.ascii_lowercase}
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        for a, e, _, b in equations:
            if e == "=":
                parent[find(a)] = find(b)
        
        for a, e, _, b in equations:
            if e == "!" and find(a) == find(b):
                return False
        return True
