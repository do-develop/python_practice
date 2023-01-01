class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # memoization approach
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if i == len(word1) or j == len(word2):
                    # sum of remaining length
                    dist = len(word1) + len(word2) - i - j
                elif word1[i] == word2[j]:
                    dist = dp(i + 1, j + 1)
                else:
                    # either one need to be deleted or replaced
                    dist = 1 + min(dp(i + 1, j), dp(i, j + 1))
                memo[i, j] = dist
            return memo[i, j]
        return dp(0, 0)
