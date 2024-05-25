class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        # BFS
        ans = []
        dq = collections.deque([(start[0], start[1], 0)])
        seen = set([(start[0], start[1])])

        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        ROWS, COLS = len(grid), len(grid[0])

        while dq:
            cx, cy, dist = dq.popleft()
            
            if pricing[0] <= grid[cx][cy] <= pricing[1]:
                ans.append([dist, grid[cx][cy], cx, cy])

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < ROWS and 0 <= ny < COLS and (nx, ny) not in seen and grid[nx][ny] > 0:
                    seen.add((nx, ny))
                    dq.append((nx, ny, dist + 1))
            
        ans.sort()
        return [x[2:] for x in ans[:k]]
