"""
Given a string s, partition s such that every substring of the partition is a
palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.
"""
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def dfs(idx):
            if idx >= len(s):
                result.append(part.copy())
                return

            for c in range(idx, len(s)):
                if self.isPalindrome(s, idx, c):
                    part.append(s[idx: c+1])
                    dfs(c + 1)
                    part.pop()

        dfs(0)
        return result

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1

        return True
            
            



# TEST
s = "aab"
print(Solution().partition(s))
# Expected Output: [["a","a","b"],["aa","b"]]
