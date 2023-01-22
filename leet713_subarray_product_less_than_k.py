class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # two pointers approach
        count, beg, end = 0, 0, 0
        product = 1
        while end < len(nums):
            product *= nums[end]
            while end >= beg and product >= k:
                product /= nums[beg]
                beg += 1
            count += end - beg + 1 # number of subarray
            end +=1
        return count
