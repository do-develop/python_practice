"""
Write a function that takes an unsigned integer and returns the number
of '1' bits it has (also known as the Hamming weight).

# Brute Force
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n > 0:
            result += n % 2
            n = n >> 1
        return result

# Bit operation
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            n = n & (n - 1)
            result += 1
        return result
"""

# python library
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

# Test
print(Solution().hammingWeight(11))