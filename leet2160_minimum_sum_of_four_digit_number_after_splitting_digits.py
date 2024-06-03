class Solution:
    def minimumSum(self, num: int) -> int:
        digits = list(str(num))
        digits.sort()
        x = digits[0] + digits[2]
        y = digits[1] + digits[3]

        return int(x) + int(y)
