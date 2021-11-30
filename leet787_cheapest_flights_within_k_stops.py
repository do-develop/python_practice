"""
There are n cities connected by some number of flights. You are given
an array flights where flights[i] = [fromi, toi, pricei] indicates that
there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest
price from src to dst with at most k stops. If there is no such route,
return -1.

# Method 1 - Using Bellman-Ford Algorithm
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):
            tmp_prices = prices.copy()

            for s, d, p in flights:  # source, destination, price:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmp_prices[d]:
                    tmp_prices[d] = prices[s] + p
            prices = tmp_prices

        return -1 if prices[dst] == float("inf") else prices[dst]
"""

from typing import List
import collections
import heapq

# Method 1 - Using Dijkstra Algorithm with HeapQ
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for s, d, p in flights:  # source, destination, price
            graph[s].append((d, p))

        # Queue variable [(price, node, possible stop count)]
        min_heap = [(0, src, k)]

        while min_heap:
            price, node, stop_count = heapq.heappop(min_heap)
            if node == dst:
                return price
            if stop_count >= 0:
                for neighbor, neigh_price in graph[node]:
                    total_price = price + neigh_price
                    heapq.heappush(min_heap, (total_price, neighbor, stop_count-1))
        return -1

# Driver Code
node_count = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
print(Solution().findCheapestPrice(node_count, edges, 0, 2, 1))
