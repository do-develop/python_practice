"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has
piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses
some pile of bananas and eats k bananas from that pile. If the pile has less
than k bananas, she eats all of them instead and will not eat any more bananas
during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before
the guards return. Return the minimum integer k such that she can eat all the
bananas within h hours.
"""
from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_speed = r

        while l <= r:
            speed = (l + r) //2
            hours = 0
            for p in piles:
                hours += math.ceil(p/speed)

            if hours <= h:
                min_speed = min(min_speed, speed)
                r = speed - 1
            else:
                l = speed + 1

        return min_speed
            




piles = [3,6,7,11]
h = 8
print(Solution().minEatingSpeed(piles, h))
# expected output: 4
