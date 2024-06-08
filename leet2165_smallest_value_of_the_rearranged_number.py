class Solution:
    def smallestNumber(self, num: int) -> int:
        
        digits = sorted(str(abs(num)))

        if num <= 0:
            return - int(''.join(digits[::-1]))
        pos = next(i for i, v in enumerate(digits) if v > '0')
        digits[pos], digits[0] = digits[0], digits[pos]

        return int(''.join(digits))
        

