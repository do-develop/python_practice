class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Time: O(N)
        dp = {}
        # DP approach
        for i in range(len(questions) -1, -1, -1):
            dp[i] = max(
                questions[i][0] + dp.get(i + 1 + questions[i][1], 0), #include
                dp.get(i + 1, 0) # skip
            )
        return dp[0]
        '''
        # backtracking approach
        def dfs(pos):
            if pos >=  len(questions):
                return 0
            
            if pos in dp:
                return dp[pos]

            dp[pos] = max(
                dfs(pos + 1), # skip question
                questions[pos][0] + dfs(pos + 1 + questions[pos][1]) # solve current question
            )

            return dp[pos]
        return dfs(0)
        '''
