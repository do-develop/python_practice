"""
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.
"""

# solution requires backtracking approach

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digit_to_char = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "qprs",
            "8": "tuv", "9": "wxyz"
        }

        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for char in digit_to_char[digits[index]]:
                dfs(index + 1, path + char)

        # handle exceptions
        if not digits:
            return []

        dfs(0, "")

        return result

print(Solution().letterCombinations("235"))