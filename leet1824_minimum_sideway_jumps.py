
'''
dp[0] = minimum jump to reach lane 1
dp[1] = minimum jump to reach lane 2
dp[2] = minimum jump to reach lane 3
If meet a stone, set its dp[i] to infinity.

'''
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [1, 0, 1]
        for lane in obstacles:
            if lane:
                dp[lane - 1] = float('inf')
            for i in range(3):
                if lane != i + 1:
                    dp[i] = min(dp[i], dp[(i + 1) % 3] + 1, dp[(i + 2) % 3] + 1)
        return min(dp)
