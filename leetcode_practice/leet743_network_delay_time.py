"""
You are given a network of n nodes, labeled from 1 to n. You are also given
times, a list of travel times as directed edges times[i] = (ui, vi, wi), where
ui is the source node, vi is the target node, and wi is the time it takes for a
signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all
the n nodes to receive the signal. If it is impossible for all the n nodes to
receive the signal, return -1.
"""
from typing import List
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((w, v))

        min_heap = [(0, k)]
        visited = set()
        t = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)

            for w2, n2 in graph[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1 + w2, n2))

        return t if len(visited) == n else -1




# TEST
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(Solution().networkDelayTime(times, n, k))
# expected output: 2
