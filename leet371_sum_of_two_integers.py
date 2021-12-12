"""
Given two integers a and b, return the sum of the two integers
without using the operators + and -.
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # to handle negative value
        INT_MAX = 0x7FFFFFFF

        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # handle negative number
        if a > INT_MAX:
            a = ~(a ^ MASK)
        return a

# Test
print(Solution().getSum(9, -11))