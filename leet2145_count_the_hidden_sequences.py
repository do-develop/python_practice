class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        x = 0
        mx, mn = 0, 0

        for diff in differences:
            x += diff
            mx = max(mx, x)
            mn = min(mn, x)
        
        return max(0, (upper - lower) - (mx - mn) + 1)
