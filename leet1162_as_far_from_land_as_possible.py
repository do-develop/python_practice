class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        # mark land in queue
        q = deque([(i,j) for i in range(row) for j in range(col) if grid[i][j] == 1])
        if len(q) == row * col or len(q) == 0:
            return -1
        # BFS approach
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for x,y in [(1,0), (-1,0), (0,1), (0,-1)]: # 4 directions
                    x1, y1 = x + r, y + c
                    if 0 <= x1 < row and 0 <= y1 < col and grid[x1][y1] == 0: # within bounds and water
                        q.append((x1, y1))
                        grid[x1][y1] = 1 # mark as visited
            level += 1
        return level - 1
