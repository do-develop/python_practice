class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        N = len(s)
        candles, plates = [], []

        for i in range(N):
            if s[i] == '|':
                candles.append(i)
        
        # binary search closest candle position
        def search_close_candle_index(candles, idx, is_first):
            l, r = 0, len(candles) - 1
            while l <= r:
                m = (l + r) // 2
                if candles[m] == idx:
                    return m
                elif candles[m] > idx:
                    r = m - 1
                else:
                    l = m + 1
            return l if is_first else r
        
        for s, e in queries:
            first_idx = search_close_candle_index(candles, s, True)
            last_idx = search_close_candle_index(candles, e, False)

            # no candles in the given interval
            if first_idx >= len(candles) or candles[last_idx] > e or candles[first_idx] < s:
                plates.append(0)
                continue
            
            num_candles = last_idx - first_idx - 1
            items = candles[last_idx] - candles[first_idx] - 1
            num_plates = max(0, items - num_candles)
            plates.append(num_plates)
        
        return plates
