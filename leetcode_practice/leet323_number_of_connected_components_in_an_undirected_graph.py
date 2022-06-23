"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge
is a pair of nodes), write a function to find the number of connected components
in an undirected graph.
"""
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()
        adj_list = [[] for i in range(n)]

        # update adjacency list
        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])

        # define dfs
        def dfs(node, adj_list, visited):
            visited.add(node)
            for a in adj_list[node]:
                if a not in visited:
                    dfs(a, adj_list, visited)
                    
        # main algorithm for the solution            
        for node in range(n):
            if node not in visited:
                dfs(node, adj_list, visited)
                count += 1
        return count
        


# TEST
n = 5
edges = [[0,1],[1,2],[3,4]]
print(Solution().countComponents(n, edges))
# expected Output: 2

"""
n = 5
edges = [[0,1],[1,2],[2,3],[3,4]]

Output: 1
"""
