class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        # sliding window approach
        seen = set()
        lo, longest = 0, 0
        for hi, c in enumerate(word):
            if hi > 0 and c < word[hi - 1]:
                seen = set()
                lo = hi
            seen.add(c)
            if len(seen) == 5:
                longest = max(longest, hi - lo + 1)
        return longest
