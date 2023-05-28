class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        max_wpi, total, cache = 0, 0, {}

        for day, hrs in enumerate(hours):
            total += 1 if hrs > 8 else -1

            if total > 0: 
                max_wpi = day + 1
            
            if not total in cache:
                cache[total] = day
            
            if total - 1 in cache:
                max_wpi = max(max_wpi, day - cache[total - 1])
        return max_wpi
