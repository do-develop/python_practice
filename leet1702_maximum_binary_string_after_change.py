# divide string into 2 parts: leading ones and the rest
# for rest part, we can always use "10" -> "01" to put all ones to the end of the string and hence move all zeros ahead of these ones;
# for all the zeros, apply "00" -> "10" from left to right, till only one "0" remaining, it is the maximum.
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        leading_ones = binary.find('0')
        if leading_ones < 0:
            return binary
        n = len(binary)
        zeros = binary.count('0')
        rest_ones = n - leading_ones - zeros
        return '1'* (leading_ones + zeros - 1) + '0' + '1' * rest_ones
