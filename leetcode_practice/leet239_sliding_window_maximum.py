"""
You are given an array of integers nums, there is a sliding window of size k
which is moving from the very left of the array to the very right. You can
only see the k numbers in the window. Each time the sliding window moves right
by one position.

Return the max sliding window.
"""

from typing import List
import collections

# dequeu approach
# Make the dequeu always in decreasing order
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        dq = collections.deque()  #store indices
        l = r = 0

        while r < len(nums):
            # pop smaller values from deque
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            #remove left val from window
            if l > dq[0]:
                dq.popleft()

            if (r+1) >= k:
                output.append(nums[dq[0]])
                l += 1
            r += 1

        return output
            


# Test
nums = [1,3,-1,-3,5,3,6,7]
window_size = 3
print(Solution().maxSlidingWindow(nums, window_size))
