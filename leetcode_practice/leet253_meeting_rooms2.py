"""
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.
"""
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        result, count = 0, 0
        s, e = 0, 0  # start array idx, end array idx
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
                
            result = max(result, count)

        return result

# TEST
intervals = [[0, 30],[5, 10],[15, 20]]
print(Solution().minMeetingRooms(intervals))
# expected output: 2
