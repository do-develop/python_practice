"""
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the
non-overlapping intervals that cover all the intervals in the input.
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn), using lambda, i is the index i[0] means the start value from pair
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            prev_end = output[-1][1]

            if start <= prev_end:
                output[-1][1] = max(prev_end, end)
            else:
                output.append([start, end])
        return output

# Test
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))