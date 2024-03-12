class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        N = len(nums)
        count = 0

        for i in range(N - 1):
            for j in range(i + 1, N):
                if nums[i] + nums[j] == target:
                    count += 1
                if nums[j] + nums[i] == target:
                    count += 1
        return count
