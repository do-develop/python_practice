"""
You are given an integer array height of length n. There are n vertical
lines drawn such that the two endpoints of the ith line are (i, 0) and
(i, height[i]). Find two lines that together with the x-axis form a
container, such that the container contains the most water. Return the
maximum amount of water a container can store.
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(area, max_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
        



# Test
height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))  # Output: 49
