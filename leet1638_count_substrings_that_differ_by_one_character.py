class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(len(t)):
                miss, pos = 0, 0
                while i + pos < len(s) and j + pos < len(t) and miss < 2:
                    miss += s[i + pos] != t[j + pos]
                    count += miss == 1
                    pos += 1
        return count
