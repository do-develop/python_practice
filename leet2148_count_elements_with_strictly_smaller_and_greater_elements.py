class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        
        nums.sort()
        valid  = len(nums)
        count_first = nums.count(nums[0])
        count_last = nums.count(nums[-1])

        valid -= (count_first + count_last)
        return valid
