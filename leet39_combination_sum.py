"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen
numbers is different.

It is guaranteed that the number of unique combinations that sum up to target
is less than 150 combinations for the given input.
"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index, combi, total):
            if total == target:
                result.append(combi[:])
                return
            if total > target:
                return

            for i in range(index, len(candidates)):
                dfs(i, combi + [candidates[i]], total + candidates[i])

        dfs(0, [], 0)
        return result

#Driver Code
candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))
            
        
