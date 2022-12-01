class Solution:
    def findComplement(self, num: int) -> int:
        res, n = 0, 0
        while num:
            # check right most bit is 0
            if not num & 1:
                # if so you have to convert it to 1 (add to the result)
                res += 2**n
            # shift bit to right until num become 0
            num >>= 1
            n += 1 # position of the next bit
        return res
