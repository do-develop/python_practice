class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        length = len(nums)
        bit_count = [0] * 32
        
        for n in nums:
            idx = 0
            while n > 0:
                if n & 1:
                    bit_count[idx] += 1
                n >>= 1
                idx += 1
        
        return sum([x * (length - x) for x in bit_count])
