class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid, need, cur = (lo + hi) // 2, 1, 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > days:
                lo = mid + 1
            else:
                hi = mid
        return lo
