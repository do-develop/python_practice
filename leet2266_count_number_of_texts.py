class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        # dynamic programming
        # count the number of texts
        mod = 10 ** 9 + 7
        N = len(pressedKeys)
        dp = [0] * (N + 1)
        dp[0] = 1 # base count

        for i in range(1, N + 1):
            dp[i] = dp[i - 1]
            if i - 2 >= 0 and pressedKeys[i-1] == pressedKeys[i-2]:
                dp[i] += dp[i - 2]
            if i - 3 >= 0 and pressedKeys[i-1] == pressedKeys[i-2] and pressedKeys[i-1] == pressedKeys[i-3]:
                dp[i] += dp[i - 3]
            
            if pressedKeys[i - 1] in {'7', '9'}:
                if i - 4 >= 0 and pressedKeys[i-1] == pressedKeys[i-2] and pressedKeys[i-1] == pressedKeys[i-3] and pressedKeys[i-1] == pressedKeys[i-4]:
                    dp[i] += dp[i - 4]
            
            dp[i] %= mod
        return dp[-1] % mod
