class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        directions = [-1, 0, 1]
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = [[False] * COLS for _ in range(ROWS)]

        # queue cells in the first column (possible starting points)
        for r in range(ROWS):
            visited[r][0] = True
            q.append((r, 0, 0)) # row, col, count

        max_moves = 0
        while q:
            size = len(q)
            for _ in range(size):
                r, c, cnt = q.popleft()
                max_moves = max(max_moves, cnt)

                for x in directions:
                    new_r, new_c = r + x, c + 1
                    if(
                        0 <= new_r < ROWS
                        and 0 <= new_c < COLS
                        and not visited[new_r][new_c]
                        and grid[r][c] < grid[new_r][new_c]
                    ):
                        visited[new_r][new_c] = True
                        q.append((new_r, new_c, cnt + 1))

        return max_moves
