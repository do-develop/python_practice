"""
Given an integer array nums and an integer k, return the k most
frequent elements. You may return the answer in any order.

Method 1 - using collections.Counter and a heapq

from typing import List
import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []

        # insert a negative value
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))  # negative frequency is the key, index is the value

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk

nums = [1, 1, 1, 2, 2, 3]
print(Solution().topKFrequent(nums, 2))
"""
# Method 2 - Pythonic way (using zip())
from typing import List
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

nums = [1, 1, 1, 2, 2, 3]
print(Solution().topKFrequent(nums, 2))
