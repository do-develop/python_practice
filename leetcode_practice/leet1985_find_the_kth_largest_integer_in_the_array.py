"""
You are given an array of strings nums and an integer k. Each string in nums
represents an integer without leading zeros. Return the string that represents
the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. For example, if nums is
["1","2","2"], "2" is the first largest integer, "2" is the second-largest
integer, and "1" is the third-largest integer.
"""
from typing import List
import heapq

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        max_heap = [-int(n) for n in nums]
        heapq.heapify(max_heap)

        while k > 1:
            heapq.heappop(max_heap)
            k -= 1

        return str(-max_heap[0])







# TEST
nums = ["3","6","7","10"]
k = 4
print(Solution().kthLargestNumber(nums, k))
"""
Output: "3"
Explanation:
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4th largest integer in nums is "3".
"""
