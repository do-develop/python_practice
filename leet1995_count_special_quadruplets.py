class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        diff_count = {}
        result = 0
        N = len(nums)
        # a + b = d - c
        for i in range(N - 2, 0 , -1):
            # d - c
            for j in range(i + 1, N):
                diff = nums[j] - nums[i]
                diff_count[diff] = diff_count.get(diff, 0) + 1
            # a + b
            for j in range(i - 2, -1, -1):
                num = nums[j] + nums[i - 1]
                result += diff_count.get(num, 0)
        return result
