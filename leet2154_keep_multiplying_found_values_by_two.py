class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        for _ in nums:
            if original in nums:
                original *= 2
        return original
