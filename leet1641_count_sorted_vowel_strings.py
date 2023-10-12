class Solution:
    def countVowelStrings(self, n: int) -> int:
        # top down approach
        '''
        seen = {}
        def dp(n, k):
            if k == 1 or n == 1:
                return k
            if (n, k) in seen:
                return seen[(n, k)]
            seen[(n, k)] = sum(dp(n - 1, k) for k in range(1, k + 1))
            return seen[(n, k)]
        return dp(n, 5)
        '''
        # bottom up approach
#                a  e  i  o  u
#     initialy: {1, 1, 1, 1, 1}   
#      n == 1 : {1, 2, 3, 4, 5}   
#      n == 2 : {1, 3, 6, 10,15}   
#      n == 3 : {1, 4, 10,20,35}    
        dp = [[0] * 6 for _ in range(n+1)]
        for i in range(1, 6):
            dp[1][i] = i
        
        for i in range(2, n+1):
            dp[i][1]=1
            for j in range(2, 6):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]  
        return dp[n][5]
