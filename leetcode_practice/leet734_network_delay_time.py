"""
You are given a network of n nodes, labeled from 1 to n. You are also given
times, a list of travel times as directed edges times[i] = (ui, vi, wi), where
ui is the source node, vi is the target node, and wi is the time it takes for
a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all
the n nodes to receive the signal. If it is impossible for all the n nodes to
receive the signal, return -1.

# Djikstra shortest path algorithm (BFS)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for src, dst, weight in times:
            graph[src].append((dst, weight))

        min_heap = [(0, k)]
        visited = set()
        total_time = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            total_time = max(total_time, w1)

            # n2 is the neighbor node of n1
            for n2, w2 in graph[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1+w2, n2))
                    
        return total_time if len(visited) == n else -1
"""

from typing import List
import collections
import heapq

# Djikstra shortest path algorithm (BFS) - optimised
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for src, dst, time in times:
            graph[src].append((dst, time))

        min_heap = [(0, k)]
        visited = collections.defaultdict(int)

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node not in visited:
                visited[node] = time
                for neighbor, neigh_time in graph[node]:
                    total_time = time + neigh_time
                    heapq.heappush(min_heap, (total_time, neighbor))
                    
                    
        return max(visited.values()) if len(visited) == n else -1


# Driver Code
if __name__ == "__main__":
    times = [[2,1,1],[2,3,1],[3,4,1]]
    node_count, start_node = 4, 2
    print(Solution().networkDelayTime(times, node_count, start_node))
