class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        beg, end = 0, max(arr)
        best, mini, diff = float("inf"), float("inf"), -1
       
        while beg <= end:
            mid = (beg + end) // 2
            total = 0

            for n in arr:
               total += min(mid, n)
            diff = abs(total - target)
            if diff == mini: # case of tie
                best = min(best, mid)
            if diff < mini: # found new best value
                mini = diff
                best = mid

            # binary search
            if total >= target:
                end = mid - 1
            else:
                beg = mid + 1
        return best
