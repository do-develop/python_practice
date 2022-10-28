class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        min_heap = []
        for r in range(min(k, rows)):
            heappush(min_heap, (matrix[r][0], r, 0))
            
        ans = -1
        for i in range(k):
            ans, r, c = heappop(min_heap)
            if c + 1 < cols:
                heappush(min_heap, (matrix[r][c+1], r, c+1))
        
        return ans
