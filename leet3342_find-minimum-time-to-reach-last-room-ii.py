class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        Row, Col = len(moveTime), len(moveTime[0])
        INF = float('inf')
        dp = [[INF] * Col for _ in range(Row)]
        heap = [(0, 0, 0)]
        visited = set()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            time, x, y = heappop(heap)

            if time >= dp[x][y]:
                continue

            if (x, y) == (Row-1, Col-1):
                return time
            dp[x][y] = time

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < Row and 0 <= ny < Col and dp[nx][ny] == INF:
                    # Move cost alternates between 1 and 2 depending on where you currently stand
                    cost = (x + y) % 2 + 1
                    nt = max(time, moveTime[nx][ny]) + cost
                    heappush(heap, (nt, nx, ny))

        return -1
