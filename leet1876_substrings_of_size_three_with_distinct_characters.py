class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        l, r = 0, 0 # window pointers
        N = len(s)
        good = 0 # count of good substrings
        while r < N:
            if r - l + 1 < k:
                r += 1
            elif r - l + 1 == k:
                if s[l] != s[l+1] and s[l+1] != s[l+2] and s[l+2] != s[l]:
                    good += 1
                # slide the window
                l += 1
                r += 1
        return good
        
