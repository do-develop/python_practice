"""
The Hamming distance between two integers is the number of positions
at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
"""
# ^ xor bit calculation
# count '1' bit only
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')


# Test
x, y = 8, 1
print(Solution().hammingDistance(x, y))
