class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res, even, odd = 0, 0, 0
        for v in arr:
            if v % 2 == 0:
                even, odd = even + 1, odd
            else:
                even, odd = odd, even + 1
            res = (res + odd) % 1_000_000_007
        return res
