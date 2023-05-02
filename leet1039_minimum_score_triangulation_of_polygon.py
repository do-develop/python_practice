class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def dfs(left, right):
            if right - left + 1 < 3:
                return 0
            minnum = float("inf")
            for mid in range(left + 1, right):
                minnum = min(minnum, values[left]* values[right]* values[mid] + dfs(left, mid) + dfs(mid, right))
            return minnum
        return dfs(0, len(values) - 1)
            
