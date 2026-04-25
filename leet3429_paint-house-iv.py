class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        dp = [
            [[float("inf") for k in range(3)] for j in range(3)] for i in range(n // 2)
        ]

        # Paint from both ends toward middle.
        for i in range(n // 2):
            # all color combinations
            for c1 in range(3):
                for c2 in range(3):
                    if c1 == c2: # should not be same color
                        continue
                    
                    dp[i][c1][c2] = cost[i][c1] + cost[n-1-i][c2]
                    if i != 0: # check previous color constraints
                        dp[i][c1][c2] += min(
                            dp[i-1][p1][p2]
                            for p1 in range(3)
                            for p2 in range(3)
                            if p1 != p2 and p1 != c1 and p2 != c2 
                        )

        return min(min(v) for v in dp[n // 2 - 1])
                        
