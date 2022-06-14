"""
Given a positive integer num, write a function which returns True if num is a
perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # O(log n)
        l, r = 1, num
        while l <= r:
            m = (l + r) // 2
            if m * m > num:
                r = m - 1
            elif m * m < num:
                l = m + 1
            else:
                return True
        return False
                    
            
        


# TEST
num = 16
print(Solution().isPerfectSquare(num))
# Output: true
