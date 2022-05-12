"""
You have a long flowerbed in which some of the plots are planted, and some are
not. However, flowers cannot be planted in adjacent plots. Given an integer
array flowerbed containing 0's and 1's, where 0 means empty and 1 means not
empty, and an integer n, return if n new flowers can be planted in the
flowerbed without violating the no-adjacent-flowers rule.
"""
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]  # to handle edge cases

        for i in range(1, len(f) - 1):  # skip first and last
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1

        return n <= 0
            
        


# TEST
flowerbed = [1,0,0,0,1]
n = 1
print(Solution().canPlaceFlowers(flowerbed, n))
#Output: true
