class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones, zeroes = 0, 0
        cur0, cur1 = 0, 0
        for c in s:
            if c == '0':
                cur0 += 1
                cur1 = 0
            else:
                cur0 = 0
                cur1 += 1
            zeroes = max(zeroes, cur0)
            ones = max(ones, cur1)
        return ones > zeroes
