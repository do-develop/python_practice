"""
Given an array intervals where intervals[i] = [li, ri] represent the interval
[li, ri), remove all intervals that are covered by another interval in the
list. The interval [a, b) is covered by the interval [c, d) if and only if
c <= a and b <= d.

Return the number of remaining intervals.
"""
from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: (i[0], -i[1]))

        result = [intervals[0]]
        for l, r in intervals[1:]:
            prevL, prevR = result[-1]

            if prevL <= l and prevR >= r:
                continue  #covered, do not count
            result.append([l, r])
        return len(result)



# TEST
intervals = [[1,4],[3,6],[2,8]]
print(Solution().removeCoveredIntervals(intervals))
#Output: 2
#Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
