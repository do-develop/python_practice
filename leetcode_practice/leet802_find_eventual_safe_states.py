"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1.
The graph is represented by a 0-indexed 2D integer array graph where graph[i]
is an integer array of nodes adjacent to node i, meaning there is an edge from
node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node
if every possible path starting from that node leads to a terminal node.

Return an array containing all the safe nodes of the graph. The answer should
be sorted in ascending order.
"""
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}

        def isSafe(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not isSafe(nei):
                    return safe[i]
            safe[i] = True  # False
            return safe[i]
                

        result = []
        for i in range(n):
            if isSafe(i):
                result.append(i)
        return result



graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(Solution().eventualSafeNodes(graph))
"""
Output: [2,4,5,6]
Explanation: Every path starting at nodes 2, 4, 5, and 6 all lead to either
node 5 or 6.
"""
