"""
There are several cards arranged in a row, and each card has an associated
number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the
row. You have to take exactly k cards. Your score is the sum of the points of
the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score
you can obtain.
"""
from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints) - k
        total = sum(cardPoints[r:])
        max_total = total

        while r < len(cardPoints):
            total += (cardPoints[l] - cardPoints[r])
            max_total = max(max_total, total)
            l += 1
            r += 1

        return max_total
        
        
        

# TEST
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(Solution().maxScore(cardPoints, k))
# expected output: 12
