"""
Given an array arr, replace every element in that array with the greatest
element among the elements to its right, and replace the last element with
-1. After doing so, return the array.
"""

from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        # reverse iteration
        # new_max = max(old_max, arr[i])

        right_max = -1

        for i in range(len(arr)-1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max
        return arr


# Test
arr = [17,18,5,4,6,1]
print(Solution().replaceElements(arr))
