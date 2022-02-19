"""
Given a string s, return the longest palindromic substring in s.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        long = ""
        for l in range(len(s)):
            for r in range(len(s)-1, l, -1):
                if len(long) >= r-l+1:
                    continue
                elif s[l:r+1] == s[l:r+1][::-1]:
                    long = s[l:r+1]
        return long

# Test
s = "babadab"
print(Solution().longestPalindrome(s))
