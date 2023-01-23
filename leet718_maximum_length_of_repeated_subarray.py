# dynamic programming approach
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        memo = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for r in range(len(nums1) -1, -1, -1):
            for c in range(len(nums2) -1, -1, -1):
                if nums1[r] == nums2[c]:
                    memo[r][c] = memo[r + 1][c + 1] + 1
        return max(max(row) for row in memo)
