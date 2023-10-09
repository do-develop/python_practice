class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # return the maximum distance between any pair of adjacent x
        # dont need to care about the y coordinates
        points.sort(key=lambda x: x[0])
        width = points[1][0] - points[0][0]
        for i in range(2, len(points)):
            width = max(points[i][0] - points[i-1][0], width)
        return width
