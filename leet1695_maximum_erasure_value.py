class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        curr_sum, max_sum, l = 0, 0, 0
        for n in nums:
            while n in seen:
                curr_sum -= nums[l]
                seen.remove(nums[l])
                l += 1
            seen.add(n)
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
        return max_sum
