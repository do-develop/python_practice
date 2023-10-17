class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # greedy approach
        res, k, pos = ['a'] * n, k - n, n - 1
        while k:
            k += 1
            if k / 26 >= 1:
                res[pos], k, pos = 'z', k - 26, pos - 1
            else:
                res[pos], k = chr(k + 96), 0
        return ''.join(res)
