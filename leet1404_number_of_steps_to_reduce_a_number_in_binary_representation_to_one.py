class Solution:
    def numSteps(self, s: str) -> int:
        l = len(s) - 1 # except the right most bit 1
        carry = count = 0

        while (l > 0):
            if int(s[l]) + carry == 0: # even number with no carry
                carry = 0
                count += 1
            elif int(s[l]) + carry == 2: # odd number with carry
                carry = 1
                count += 1
            else: # odd case (even num with carry 1 or odd num with carry 0)
                carry = 1
                count += 2
            l -= 1
        
        # last digit (right most bit 1) 
        if carry == 1:
            count += 1
        return count
