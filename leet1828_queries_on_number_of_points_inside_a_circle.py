class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # (x, y) inside the circle if met,
        # (circle_center_x - x1) ^ 2 + (circle_center_y - y1) ^ 2 <= r * r
        lis=[]
        for circle in queries:
            cnt=0
            for pt in points:
                if ((((circle[0]-pt[0])**2)+((circle[1]-pt[1])**2))**0.5)<=circle[2]:
                    cnt+=1
            lis.append(cnt)
        return lis
