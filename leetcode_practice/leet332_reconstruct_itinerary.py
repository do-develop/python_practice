"""
You are given a list of airline tickets where tickets[i] =
[fromi, toi] represent the departure and the arrival airports
of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus,
the itinerary must begin with "JFK". If there are multiple valid
itineraries, you should return the itinerary that has the smallest
lexical order when read as a single string.


# Method 1 - Using Queue
from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # construct the dictionary, graph
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop(0))
            route.append(start)

        dfs('JFK')
        # reverse the order to get the smaller lexical order
        return route[::-1]

# Method 2 - Using Stack
from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # construct the dictionary, graph
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            route.append(start)

        dfs('JFK')
        # reverse the order to get the smaller lexical order
        return route[::-1]
"""

# Method 2 - Using iterative approach
from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # construct the dictionary, graph
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []
        stack = ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        # reverse the order to get the smaller lexical order
        return route[::-1]

# Driver Code
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(Solution().findItinerary(tickets))
