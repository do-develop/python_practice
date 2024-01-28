class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        prepos = res = 0

        for pos in rungs:
            # -1, as it doesn't need another rung if the distance
            # between two rungs is less then and equal to dist
            res += (pos - prepos - 1) // dist
            prepos = pos
        return res
