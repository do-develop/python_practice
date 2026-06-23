class Solution:
    MOD = 10**9 + 7

    def dfs(self, graph: list, x:int, parent:int) -> int:
        max_depth = 0
        for y in graph[x]:
            # if this neighbor is my parent, skip it
            if y == parent:
                continue
            # recurse into the neighbor, then add 1 for this edge
            max_depth = max(max_depth, self.dfs(graph, y, x) + 1)
        return max_depth

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        N = len(edges) + 1 
        graph = [[] for _ in range(N + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        max_depth = self.dfs(graph, 1, 0)

        # Each edge on the longest path can be weight 1 or 2,
        # so there are 2^(max_depth - 1) valid assignments
        return pow(2, max_depth - 1, self.MOD)
