"""
There are n cities connected by some number of flights. You are given an array
flights where flights[i] = [fromi, toi, pricei] indicates that there is a
flight from city fromi to city toi with cost pricei. You are also given three
integers src, dst, and k, return the cheapest price from src to dst with at
most k stops. If there is no such route, return -1.
"""
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            temp_prices = prices.copy()
            
            for s, d, p in flights:  # s=source, d=destination, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < temp_prices[d]:
                    temp_prices[d] = prices[s] + p

            prices = temp_prices

        return -1 if prices[dst] == float("inf") else prices[dst]
        
        





# TEST
n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
print(Solution().findCheapestPrice(n, flights, src, dst, k))
#Output: 500
