class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = s.count(s[0])
        for i in range(1, len(s)):
            if s.count(s[i]) != freq:
                return False
        return True
