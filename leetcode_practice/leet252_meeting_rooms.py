"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
"""
from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda i:i[0])

        prev = None

        for i in intervals:
            if prev and i[0] < prev[1]:
                return False
            prev = i
            
        return True

        

# TEST
intervals = [[0,30],[5,10],[15,20]]
print(Solution().canAttendMeetings(intervals))
"""
intervals = [[7,10],[2,4]]
Output: true

intervals = [[0,30],[5,10],[15,20]]
Output: false
"""
