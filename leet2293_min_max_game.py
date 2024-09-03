class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        while len(nums) > 1:
            N = len(nums)
            curr = [0] * (N // 2)
            for i in range(N // 2):
                if i % 2 == 0:
                    curr[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    curr[i] = max(nums[2 * i], nums[2 * i + 1])
            nums = curr
        return nums[0]
