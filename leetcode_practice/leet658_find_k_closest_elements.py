"""
Given a sorted integer array arr, two integers k and x, return the k closest
integers to x in the array. The result should also be sorted in ascending order.
"""
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # handle edge cases
        if len(arr) == 1:
            return arr

        if x < arr[0]:
            return arr[0:k]
        elif x > arr[-1]:
            return arr[-k::]

        # Find index of x or the closest val to x
        l, r = 0, len(arr) - 1
        val, idx = arr[0], 0
        while l <= r:
            m = (l + r) // 2
            curDiff, prevDiff = abs(arr[m] - x), abs(val - x)
            if (curDiff < prevDiff or
                (curDiff == prevDiff and arr[m] < val)):
                val, idx = arr[m], m

            if arr[m] < x: l = m + 1
            elif arr[m] > x: r = m - 1
            else: break

        l = r = idx
        for i in range(k - 1):
            if l == 0:
                r += 1
            elif r == len(arr) - 1 or x - arr[l-1] <= arr[r+1] - x:
                l -= 1
            else:
                r += 1
        return arr[l:r+1]
            
        

arr = [1,2,3,4,5]
k = 4
x = 3
print(Solution().findClosestElements(arr, k, x))
# Output: [1,2,3,4]        
