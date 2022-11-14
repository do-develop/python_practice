class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        
        for i in range(len(p) - 1, len(s)):
            sCounter [s[i]] += 1
            if sCounter == pCounter:
                res.append(i - len(p) + 1)      # append the starting index
            sCounter[s[i - len(p) + 1]] -= 1    # decrement left most char frequency
            if sCounter[s[i - len(p) + 1]] == 0:
                del sCounter[s[i - len(p) + 1]]
        
        return res
