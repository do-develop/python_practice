class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        factor_sum = 1
        for i in range(2, ceil(num ** 0.5)):
            if num % i == 0:
                # square root, only add once
                if i == num // i: 
                    factor_sum += i
                else:
                    factor_sum += i + (num // i)
        
        return factor_sum == num
