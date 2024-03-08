class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini = diff = 0
        N = len(nums)

        for i in range(N - 1):
            for j in range(i + 1, N):
                if nums[i] < nums[j]:
                    diff = nums[j] - nums[i]
                    if diff >= mini:
                        mini = diff

        return -1 if mini == 0 else mini
