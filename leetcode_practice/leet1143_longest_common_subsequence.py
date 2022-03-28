"""
Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0. A subsequence of a
string is a new string generated from the original string with some characters
(can be none) deleted without changing the relative order of the remaining
characters. For example, "ace" is a subsequence of "abcde". A common subsequence
of two strings is a subsequence that is common to both strings.
"""
# Dynamic programming - finding sub-problem
# 2 dimensional dynamic programming problem
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for c in range(len(text2)+1)] for r in range(len(text1)+1)]

        for r in range(len(text1) - 1, -1, -1):
            for c in range(len(text2) -1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r][c+1], dp[r+1][c])
        return dp[0][0]
              
        




text1 = "abcde"
text2 = "bce"
print(Solution().longestCommonSubsequence(text1, text2))
# expected output: 3  
