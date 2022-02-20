"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # ptr to A mid point
            j = half - i - 2 # ptr to (A + B) mid point

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if i+1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if j+1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                # odd number of elements
                if total % 2:
                    return min(Aright, Bright)
                # even
                return max(Aleft, Bleft) + min(Aright, Bright) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


# TEST
nums1 = [1,2]
nums2 = [3,4]
print(Solution().findMedianSortedArrays(nums1, nums2))
# Expected Output: 2.50000 --> Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
