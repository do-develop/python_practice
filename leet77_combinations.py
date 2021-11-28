"""
Given two integers n and k, return all possible combinations of
k numbers out of the range [1, n].

# Method 1 - using python library
import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))

# Method 2 - using backtracking approach
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, combination: int):
            if combination == 0:
                results.append(elements[:])

            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, combination-1)
                elements.pop()

        dfs([], 1, k)
        return results

"""
from typing import List

# Method 2 - using backtracking approach
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb[:])  # add the comb.copy()
                return
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()

        backtrack(1, [])
        return res

print(Solution().combine(4, 2))