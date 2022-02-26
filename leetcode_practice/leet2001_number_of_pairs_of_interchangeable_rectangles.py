"""
You are given n rectangles represented by a 0-indexed 2D integer array
rectangles, where rectangles[i] = [widthi, heighti] denotes the width and
height of the ith rectangle. Two rectangles i and j (i < j) are considered
interchangeable if they have the same width-to-height ratio. More formally,
two rectangles are interchangeable if widthi/heighti == widthj/heightj (using
decimal division, not integer division).

Return the number of pairs of interchangeable rectangles in rectangles.
"""
from typing import List

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}  # w/h: count

        for w, h in rectangles:
            count[w/h] = 1 + count.get(w/h, 0)

        result = 0
        for c in count.values():
            if c > 1:
                result += (c*(c-1)) // 2
        return result
        
        



# TEST
rectangles = [[4,8],[3,6],[10,20],[15,30]]
print(Solution().interchangeableRectangles(rectangles))
"""
Output: 6
Explanation: The following are the interchangeable pairs of rectangles by index (0-indexed):
- Rectangle 0 with rectangle 1: 4/8 == 3/6.
- Rectangle 0 with rectangle 2: 4/8 == 10/20.
- Rectangle 0 with rectangle 3: 4/8 == 15/30.
- Rectangle 1 with rectangle 2: 3/6 == 10/20.
- Rectangle 1 with rectangle 3: 3/6 == 15/30.
- Rectangle 2 with rectangle 3: 10/20 == 15/30.
"""
