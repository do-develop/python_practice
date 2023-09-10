class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        prev = '0'
        for i in range(n - 1):
            prev = prev + '1' + self.inv_and_rev(prev)
        return prev[k - 1]

    def inv_and_rev(self, s):
        ans = ""
        for c in s[::-1]:
            if c == '0':
                ans += '1'
            else:
                ans += '0'
        return ans
