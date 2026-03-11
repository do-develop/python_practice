class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        Row, Col = len(moveTime), len(moveTime[0])
        heap = [(0, 0, 0)]
        visited = set()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            time, x, y = heappop(heap)

            if (x, y) in visited:
                continue
            visited.add((x, y))

            if (x, y) == (Row-1, Col-1):
                return time

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < Row and 0 <= ny < Col:
                    nt = max(time, moveTime[nx][ny]) + 1
                    heappush(heap, (nt, nx, ny))

        return -1
