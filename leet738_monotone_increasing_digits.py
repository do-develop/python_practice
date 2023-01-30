class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # handle edge case
        if n < 10: return n
        number, inv_idx = n, -1
        num = [int(digit) for digit in str(number)[::-1]]

        for i in range(1, len(num)):
            if num[i] > num[i - 1] or (inv_idx != -1 and num[inv_idx] == num[i]):
                inv_idx = i
        # is it already in monotonically increasing order
        if inv_idx == -1: 
            return n

        for i in range(inv_idx):
            num[i] = 9
        num[inv_idx] -= 1

        return int(''.join([str(i) for i in num[::-1]]))
