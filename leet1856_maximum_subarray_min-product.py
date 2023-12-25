class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        prefsum = [0]
        stack = [-1]
        nums.append(0)
        res = 0

        for i in range(len(nums)):
            while nums[stack[-1]] > nums[i]:
                min_val = nums[stack.pop()]
                range_sum = prefsum[i] - prefsum[stack[-1] + 1] # important to +1 here.it is non inclusive boundary
                res = max(res, range_sum * min_val)
            stack.append(i)
            prefsum.append(prefsum[-1] + nums[i])
        return res % mod
