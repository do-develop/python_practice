class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_dist = idx1 = 0

        for idx2, val2 in enumerate(nums2):
            while idx1 < len(nums1) and nums1[idx1] > val2:
                idx1 += 1
            if idx1 == len(nums1):
                break
            max_dist = max(max_dist, idx2 - idx1)
        return max_dist
