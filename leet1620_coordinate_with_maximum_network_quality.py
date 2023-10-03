class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        mx, ans = -1, [0, 0]
        def get_quality(dx, dy):
            nonlocal radius
            dist = sqrt(dx*dx + dy*dy)
            return 0 if dist > radius else 1/(1 + dist)

        for x in range(51):
            for y in range(51):
                total = sum(floor(q * get_quality(abs(x-tx), abs(y-ty))) for tx, ty, q in towers)
                if total > mx:
                    mx, ans = total, [x, y]
        
        return ans
