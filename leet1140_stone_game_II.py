class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}
        # the num of stones alice gets
        def dfs(alice, i, M):
            if i == len(piles):
                return 0
            if (alice, i, M) in cache:
                return cache[(alice, i, M)]
            res = 0 if alice else float("inf")
            total = 0 # prefix sum
            for X in range(1, 2 * M + 1):
                if i + X > len(piles): # bound check
                    break
                total += piles[i + X - 1]
                # alice's turn, maximise her score
                if alice:
                    res = max(res, total + dfs(False, i + X, max(M, X)))
                else:
                # bob's turn, minimise alice's score
                    res = min(res, dfs(True, i + X, max(M, X)))
            cache[(alice, i, M)] = res
            return res
        return dfs(True, 0, 1)
