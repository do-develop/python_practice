class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        area = float('inf')
        seen = {}
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i + 1:]:
                cx = (x1 + x2) / 2
                cy = (y1 + y2) / 2
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2 # distance
                # same center and same distance already visited?
                for sx, sy in seen.get((cx, cy, d), []):
                    cur_area = sqrt(((x1 - sx) ** 2 + (y1 - sy) ** 2) * \
                                    ((x2 - sx) **2 + (y2 - sy) ** 2))
                    area = min(area, cur_area)
                seen.setdefault((cx, cy, d), []).append((x1, y1))
        return area if area < float('inf') else 0
