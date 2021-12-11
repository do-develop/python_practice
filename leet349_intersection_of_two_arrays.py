"""
Given two integer arrays nums1 and nums2, return an array of
their intersection. Each element in the result must be unique
and you may return the result in any order.

# Brute Force
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: set = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    result.add(n1)
        return result

# Binary Search
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: set = set()
        nums2.sort()
        for n1 in nums1:
            idx2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > idx2 and n1 == nums2[idx2]:
                result.add(n1)
        return result
"""
import bisect
from typing import List

# Two pointers approach
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: set = set()
        nums1.sort()
        nums2.sort()
        # two pointers
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1

        return result

# Test
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

print(Solution().intersection(nums1, nums2))