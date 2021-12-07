"""
Given two strings s and t, return true if t is an
anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
"""

# using hashmap character as key and count of the character as value
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

# Test
s = "anagram"
t = "nagaram"

print(Solution().isAnagram(s, t))
