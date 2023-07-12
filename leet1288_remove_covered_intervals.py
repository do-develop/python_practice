class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # sort left ascending and right decending
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        count = prev_r = 0

        for l, r in intervals:
            count += r > prev_r
            prev_r = max(prev_r, r)

        return count
        
