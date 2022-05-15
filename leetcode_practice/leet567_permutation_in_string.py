"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1,
or false otherwise. In other words, return true if one of s1's permutations is
the substring of s2.
"""
import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = collections.Counter(s1)

        for i in range(len(s2) - len(s1) + 1):
            if collections.Counter(s2[i:i+len(s1)]) == s1_counter:
                return True
        return False

# TEST
s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))
"""
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
"""
