class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def feasible(cur_day) -> bool:
            bouquets = adj_flowers = 0
            for day in bloomDay:
                if day > cur_day:
                    adj_flowers = 0
                else:
                    bouquets += (adj_flowers + 1) // k
                    adj_flowers = (adj_flowers + 1) % k
            return bouquets >= m

        if len(bloomDay) < m * k:
            return -1
        l, r = 1, max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l
