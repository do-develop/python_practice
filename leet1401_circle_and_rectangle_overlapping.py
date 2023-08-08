class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # for a point (x, y) to be inside the circle, it has to satisfy the following:
        # (x - x_center) ^ 2 + (y - y_center) ^ 2 <= radius ^ 2
        for (x, y) in [(x1,y1), (x1,y2), (x2,y1), (x2,y2)]:
            if (xCenter - x) ** 2 + (yCenter - y) ** 2 <= radius ** 2:
                return True
        # for a point (x, y) to be inside the rectangle
        # x1 <= x <= x2
        # y1 <= y <= y2
        for x in [x1, x2]:
            if xCenter - radius <= x <= xCenter + radius and y1 <= yCenter <= y2:
                return True
        for y in [y1, y2]:
            if yCenter - radius <= y <= yCenter + radius and x1 <= xCenter <= x2:
                return True
        # the circle is completely inside the rectangle
        return x1 <= xCenter <= x2 and y1 <= yCenter <= y2
