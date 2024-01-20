class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        odd = even = 0
        for n in nums:
            odd = max(odd, even - n)
            even = max(even, odd + n)
        return even # will always have even >= odd
