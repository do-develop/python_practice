"""
Given a string s, return the longest palindromic substring in s.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # check palindrome and expand two pointers
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left + 1: right - 1]

        # quick first check
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        # move to the right
        for i in range(len(s)-1):
            result = max(result,
                         expand(i, i+1),
                         expand(i, i+2),
                         key=len)
        return result

obj = Solution()
print(obj.longestPalindrome("babad"))