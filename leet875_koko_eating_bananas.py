class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # min tine unit to max time unit
        min_speed = r

        # binary search
        while l <= r:
            m = (l + r) // 2
            total_hour = 0
            for p in piles:
                total_hour += math.ceil(p / m)
            if total_hour <= h:
                r = m - 1
                min_speed = min(min_speed, m)
            else:
                l = m + 1
        return min_speed
        



                
            
        
