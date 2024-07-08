class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        @lru_cache(None) # cache can grow without any limiations
        def dp(k, numArrows):
            if k == 12 or numArrows <= 0:
                return 0
            # two cases
            # 1) Bob loses
            max_score = dp(k + 1, numArrows)
            # 2) Bob wins
            if numArrows > aliceArrows[k]:
                max_score = max(max_score, dp(k + 1, numArrows - aliceArrows[k] - 1) + k)
            return max_score
        
        # backtracking
        bobArrows = [0] * 12
        for k in range(12):
            if dp(k, numArrows) != dp(k + 1, numArrows): # bob wins!
                bobArrows[k] = aliceArrows[k] + 1
                numArrows -= bobArrows[k]

        if numArrows > 0: # handling remaining arrows
            bobArrows[0] += numArrows
        return bobArrows
