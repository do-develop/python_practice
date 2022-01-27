"""
Given an array nums of distinct integers, return all the possible
permutations. You can return the answer in any order.

import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))

"""
from typing import List
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []

        def dfs(elements):
            # if reached the leaf node add the result
            if len(elements) == 0:
                result.append(prev_elements[:])  # add shallow copy of a list

            # create permutation through recursive calls
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return result

# Driver Code
print(Solution().permute([1,2,3]))
