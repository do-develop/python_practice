"""
Given two strings s and p, return an array of all the start indices of p's
anagrams in s. You may return the answer in any order. An Anagram is a word or
phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pCount, sCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        result = [0] if sCount == pCount else []
        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1

            if sCount == pCount:
                result.append(l)
        return result


# TEST
s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))
"""
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""
