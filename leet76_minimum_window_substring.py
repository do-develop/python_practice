"""
Given two strings s and t of lengths m and n respectively, return the
minimum window substring of s such that every character in t (including
duplicates) is included in the window. If there is no such substring,
return the empty string "".

The testcases will be generated such that the answer is unique.
A substring is a contiguous sequence of characters within the string.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        have, need = 0, len(countT)
        result, result_len = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                # update result
                if (r -l +1) < result_len:
                    result = [l, r]
                    result_len = (r - l + 1)
                 # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l,r = result
        return s[l:r+1] if result_len != float("infinity") else ""

s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))