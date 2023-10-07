class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols, dx, dy = len(heights), len(heights[0]), 1, 0
        ans, heap, unseen = 0, [(0, 0, 0)], set(product(range(rows), range(cols)))

        while heap:
            effort, x, y = heappop(heap)
            unseen.discard((x, y))
            ans = max(ans, effort)
            if(x, y) == (rows-1, cols-1): break

            for _ in range(4): # 4 directions
                nx, ny, dx, dy = x + dx, y + dy, -dy, dx
                if (nx, ny) in unseen:
                    heappush(heap, (abs(heights[x][y] - heights[nx][ny]), nx, ny))
        return ans
