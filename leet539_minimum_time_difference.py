class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # convert time to minutes
        def convert(t):
            return 60 * int(t[:2]) + int(t[3:])

        max_minutes = 60 * 24
        if len(timePoints) > max_minutes: # there must be a duplicate
            return 0
        
        # sort the time so the smallest diff will always be diff btw two neighbors
        times = [convert(t) for t in timePoints]
        times.sort()

        min_diff = max_minutes
        for i in range(1, len(times)):
            hi_time = times[i]
            lo_time = times[i - 1]
            min_diff = min(min_diff, hi_time - lo_time)
        # edge case: 24 hours clock check the first and the last time
        min_diff = min(min_diff, (times[0] - times[-1]) % max_minutes)

        return min_diff
