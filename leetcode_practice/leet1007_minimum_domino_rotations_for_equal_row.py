"""
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves
of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on
each half of the tile.) We may rotate the ith domino, so that tops[i] and
bottoms[i] swap values. Return the minimum number of rotations so that all the
values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.
"""
from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for target in [tops[0], bottoms[0]]:
            missingT, missingB = 0, 0
            for i in range(len(tops)):
                if not(tops[i] == target or bottoms[i] == target):
                    break
                if tops[i] != target:
                    missingT += 1
                if bottoms[i] != target:
                    missingB += 1
                if i == len(tops) - 1:
                    return min(missingT, missingB)



tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
print(Solution().minDominoRotations(tops, bottoms))
#Output: 2
"""
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before
we do any rotations. If we rotate the second and fourth dominoes, we can make
every value in the top row equal to 2, as indicated by the second figure.
"""
