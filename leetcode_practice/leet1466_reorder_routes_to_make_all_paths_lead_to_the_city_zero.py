"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is
only one way to travel between two different cities (this network form a tree).
Last year, The ministry of transport decided to orient the roads in one direction
because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents
a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people
want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the
city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.
"""
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # start at city 0
        # recursively check its neighbors
        # count outgoint edges

        edges = {(a,b) for a, b in connections}  # hash set
        neighbors = {city:[] for city in range(n)}
        visited = set()
        changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal edges, neighbors, visited, changes

            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue

                #check if this neighbor can reach city 0
                if (neighbor, city) not in edges:
                    changes += 1

                visited.add(neighbor)
                dfs(neighbor)
        visited.add(0)
        dfs(0)

        return changes

        

# Test
cities = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(Solution().minReorder(cities, connections))
