"""
A tree is an undirected graph in which any two vertices are connected by
exactly one path. In other words, any connected graph without simple cycles
is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges
where edges[i] = [ai, bi] indicates that there is an undirected edge between
the two nodes ai and bi in the tree, you can choose any node of the tree as
the root. When you select a node x as the root, the result tree has height h.
Among all possible rooted trees, those with minimum height (i.e. min(h))  are
called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.
"""
from typing import List
import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]  # there should be at least 2 nodes to make up a tree

        # Form a bi-directional graph
        graph = collections.defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        # declare and initialise a variable for leaves
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # until there is 1 or 2 nodes left remove leaves
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves

# Driver Code
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print(Solution().findMinHeightTrees(n, edges))