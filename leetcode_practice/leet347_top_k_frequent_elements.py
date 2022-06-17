"""
Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.
"""
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq)-1, -1, -1):
            for f in freq[i]:
                result.append(f)
                if len(result) == k:
                    return result



# TEST
nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))
# expected output: [1,2]
