class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0

        for c in letters:
            l, r = s.index(c), s.rindex(c)
            between = set()

            for i in range(l + 1, r):
                between.add(s[i])
            ans += len(between)

        return ans
