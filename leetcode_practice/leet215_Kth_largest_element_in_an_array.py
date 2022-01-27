"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Using the built-in Timsort - Fastest performance
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]


# Quick select approach
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_idx = len(nums) - k

        def quickSelect(l, r):
            pivot, partition = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[partition], nums[i] = nums[i], nums[partition]
                    partition += 1
            nums[partition], nums[r] = nums[r], nums[partition]

            if partition > k:
                return quickSelect(l, partition - 1)
            elif k > partition:
                return quickSelect(partition + 1, r)
            else:
                return nums[partition]
        return quickSelect(0, len(nums) - 1)

# heapq approach
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)  # to achieve max heap

        for _ in range(k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)


# using heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
"""
from typing import List
import heapq

# using heapq.nlargest
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

