class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        for r in range(len(s)): # increase the right window
            cost = abs(ord(s[r]) - ord(t[r]))
            maxCost -= cost
            if maxCost < 0: # reduce the left window
                maxCost += abs(ord(s[l]) - ord(t[l]))
                l += 1
        return r - l + 1 # window size
