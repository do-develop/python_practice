class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # time = distance/speed
        # binary search the min speed
        lo, hi = 1, int(1e7)
        min_speed = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.isPossible(dist, mid, hour):
                min_speed = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return min_speed
    
    def isPossible(self, dist:List[int], speed:int, hour: float):
        total_time = 0
        for i in range(len(dist)):
            time = dist[i] * 1.0 / speed
            if i != len(dist) - 1: # not the final destination
                total_time += math.ceil(time)
            else:
                total_time += time
            if total_time > hour:
                return False
        return total_time <= hour
