"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            result += self.countPalindrome(i, i)
            result += self.countPalindrome(i, i+1)
        return result

    def countPalindrome(self, l, r):
        count = 0
        while (l >= 0 and r < len(s) and s[l]==s[r]):
            count += 1
            l -= 1
            r += 1
        return count




# TEST
s = "aaa"
print(Solution().countSubstrings(s))
# expected utput: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
