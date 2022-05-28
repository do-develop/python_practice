"""
Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest of
the intervals non-overlapping.
"""
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        min_remove = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                min_remove += 1
                prevEnd = min(end, prevEnd)  # keep the small end
        return min_remove
        

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(Solution().eraseOverlapIntervals(intervals))
"""
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are
non-overlapping.
"""
