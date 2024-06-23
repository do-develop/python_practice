class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # DFS approach
        direct_child = defaultdict(list)
        ans = [[] for _ in range(n)]

        for x, y in edges:
            direct_child[x].append(y)
        
        def dfs(ancestor, me):
            for child in direct_child[me]:
                # does the child has the ancestor already?
                if ans[child] and ans[child][-1] == ancestor:
                    continue
                ans[child].append(ancestor)
                dfs(ancestor, child)
        
        for i in range(n):
            dfs(i, i)
        return ans
