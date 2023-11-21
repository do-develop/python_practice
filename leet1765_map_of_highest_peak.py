class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        height = [[-1] * cols for _ in range(rows)]
        q = deque([])
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    q.append((r,c))
                    height[r][c] = 0

        dir = [[0,1], [1,0], [0,-1], [-1, 0]]
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dir[i][0], c + dir[i][1]
                if nr < 0 or nr == rows or nc < 0 or nc == cols or height[nr][nc] != -1:
                    continue
                height[nr][nc] = height[r][c] + 1
                q.append((nr,nc))
        return height
