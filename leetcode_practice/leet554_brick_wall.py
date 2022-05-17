"""
There is a rectangular brick wall in front of you with n rows of bricks. The
ith row has some number of bricks each of the same height (i.e., one unit) but
they can be of different widths. The total width of each row is the same. Draw
a vertical line from the top to the bottom and cross the least bricks. If your
line goes through the edge of a brick, then the brick is not considered as
crossed. You cannot draw a line just along one of the two vertical edges of the
wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return
the minimum number of crossed bricks after drawing such a vertical line.
"""
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count_gap = { 0: 0}

        for r in wall:
            position = 0
            for b in r[:-1]:
                position += b
                count_gap[position] = 1 + count_gap.get(position, 0)

        return len(wall) - max(count_gap.values())
    



# TEST
wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
print(Solution().leastBricks(wall))
# expected output: 2
