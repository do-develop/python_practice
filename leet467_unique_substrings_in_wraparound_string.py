class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        substr = {i: 1 for i in p}
        count = 1
        for c1, c2 in zip(p, p[1:]):
            # %26 for wraparound (za)
            # only one char away == substring
            count = count + 1 if (ord(c2) - ord(c1)) % 26 == 1 else 1
            substr[c2] = max(substr[c2], count)
        return sum(substr.values())
        
