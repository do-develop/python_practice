class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        # case 1: for each idx in nums if every elem before is smaller and every elem after is bigger
        # case 2: if not case 1, simply compare left and right, of condition satisfies increment by 1

        # to check all elements after element at this position is smaller
        N = len(nums)
        minis = [None for _ in range(N)]
        mini = float('-inf')
        for i in range(N):
            minis[i] = mini
            mini = max(nums[i], mini)
        
        # all elements after element at this position is bigger?
        maxis = [None for _ in range(N)]
        maxi = float('inf')
        for i in range(N-1, -1, -1):
            maxis[i] = maxi
            maxi = min(nums[i], maxi)

        total = 0
        for i in range(1, N - 1):
            if minis[i] < nums[i] < maxis[i]:
                total += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                total += 1
        return total
