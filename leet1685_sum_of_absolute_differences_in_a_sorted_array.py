class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # O(N) using prefix sum
        n = len(nums)
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(prefix[-1] + nums[i])
        
        ans = []
        for i in range(n):
            left_sum = prefix[i] - nums[i]
            right_sum = prefix[-1] - prefix[i]

            left_cnt = i
            right_cnt = n - 1 - i

            left_total = left_cnt * nums[i] - left_sum
            right_total = right_sum - right_cnt * nums[i]

            ans.append(left_total + right_total)
        return ans
