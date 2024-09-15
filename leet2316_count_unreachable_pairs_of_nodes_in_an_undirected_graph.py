class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # get the size of all components in the graph
        def dfs(node, neighbors, visited):
            visited[node] = True
            ans = 1

            for neigh in neighbors[node]:
                if not visited[neigh]:
                    ans += dfs(neigh, neighbors, visited)
            return ans

        # find the products of all possible pairs
        neighbors = [[] for _ in range(n)]
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
        
        visited = [False] * n
        total, square_total = 0, 0

        for i in range(n):
            if not visited[i]:
                ans = dfs(i, neighbors, visited)
                total += ans
                square_total += ans * ans
        return (total * total - square_total) // 2
