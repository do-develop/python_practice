"""
Given an array of strings strs, group the anagrams together. You can return the
answer in any order. An Anagram is a word or phrase formed by rearranging the
letters of a different word or phrase, typically using all the original letters
exactly once.
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        return result.values()
            



# TEST
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))
# Expected Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
