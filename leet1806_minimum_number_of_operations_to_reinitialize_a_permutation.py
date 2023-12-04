class Solution:
    def reinitializePermutation(self, n: int) -> int:
        res, idx = 0, 1
        # until find the inverse
        while res == 0 or idx > 1:
            if idx < n / 2:
                idx *= 2
            else:
                idx = (idx - n / 2) * 2 + 1
            res += 1
        return res
