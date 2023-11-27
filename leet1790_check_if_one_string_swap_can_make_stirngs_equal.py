class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff1 = -1
        diff2 = -1

        for idx in range(len(s1)):
            if s1[idx] != s2[idx]:
                if diff1 == -1:
                    diff1 = idx
                elif diff2 == -1:
                    diff2 = idx
                else: # found more than 2 differences
                    return False
        return s1[diff1] == s2[diff2] and s1[diff2] == s2[diff1]
