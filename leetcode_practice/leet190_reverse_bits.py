"""
Reverse bits of a given 32 bits unsigned integer.

Note:
Note that in some languages, such as Java, there is no unsigned integer type.
In this case, both input and output will be given as a signed integer type.
They should not affect your implementation, as the integer's internal binary
representation is the same, whether it is signed or unsigned.

In Java, the compiler represents the signed integers using 2's complement
notation. Therefore, in Example 2 above, the input represents the signed
integer -3 and the output represents the signed integer -1073741825.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << (31 - i))
        return result
            
            





# TEST
n = 11111111111111111111111111111101
print(Solution().reverseBits(n))
"""
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101
represents the unsigned integer 4294967293, so return 3221225471 which its
binary representation is 10111111111111111111111111111111.
"""
