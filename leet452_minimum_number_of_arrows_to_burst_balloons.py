class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort by end value
        points.sort(key=lambda x:x[1])
        # handle edge case
        length = len(points)
        if length == 0: 
            return 0
        # initialise variable
        curr, count = points[0], 1
        
        for i in range(1, length):
            if curr[1] < points[i][0]: # doesn't overlap?
                count += 1
                curr = points[i]
        return count
