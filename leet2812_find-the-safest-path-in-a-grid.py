class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        thieves = []
        Rows, Cols = len(grid), len(grid[0])
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    thieves.append([r, c])

        visited = [[0 for c in range(Cols)] for r in range(Rows)]
        distance = [[0 for c in range(Cols)] for r in range(Rows)]

        # minimum manhatten distance of each cell to thieves
        depth = 0
        while thieves:
            temp = []
            for r, c in thieves:
                if not visited[r][c]:
                    visited[r][c] = 1
                    distance[r][c] = depth
                    for x, y in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                        if 0 <= x < Rows and 0 <= y < Cols:
                            temp.append([x, y])
            thieves = temp
            depth += 1

        visited = [[0 for c in range(Cols)] for r in range(Rows)]
        pq = [[-distance[0][0], 0, 0]]
        while pq:
            dist, r, c = heapq.heappop(pq)
            if visited[r][c]:
                continue
            visited[r][c] = 1
            if r == Rows - 1 and c == Cols - 1:
                return -dist

            for x, y in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= x < Rows and 0 <= y < Cols:
                    heapq.heappush(pq, [-min(-dist, distance[x][y]), x, y])

        return -1
