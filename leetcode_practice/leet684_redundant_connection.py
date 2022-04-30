"""
In this problem, a tree is an undirected graph that is connected and has no
cycles. You are given a graph that started as a tree with n nodes labeled from
1 to n, with one additional edge added. The added edge has two different
vertices chosen from 1 to n, and was not an edge that already existed. The
graph is represented as an array edges of length n where edges[i] = [ai, bi]
indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n
nodes. If there are multiple answers, return the answer that occurs last in
the input.
"""
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [0] * (len(edges) + 1)

        def find(x):
            if parents[x] == 0:
                return x
            return find(parents[x])

        for x, y in edges:
            a = find(x)
            b = find(y)
            if a == b:
                return [x,y]
            if(a < b):
                parents[b] = a
            else:
                parents[a] = b




# TEST
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(Solution().findRedundantConnection(edges))
# expected output: [1,4]
