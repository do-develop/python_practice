class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        cur = res = 0
        for v in values:
            res = max(res, cur + v)
            cur = max(cur, v) - 1
        return res
