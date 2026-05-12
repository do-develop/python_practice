class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        candidates = []

        for i in range(len(grid)):
            s = sorted(grid[i], reverse=True)
            candidates.extend(s[:limits[i]])

        candidates.sort()
        total = 0

        for i in range(k):
            total += candidates.pop()
        
        return total
