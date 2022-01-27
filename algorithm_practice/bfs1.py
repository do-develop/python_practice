from collections import deque

row, col = map(int, input().split())
graph = []
for i in range(row):
    graph.append(list(map(int, input())))

# 4 directions
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # check bounds
            if new_x < 0 or new_y < y or new_x >= row or new_y >= col:
                continue
            # check walls
            if graph[new_x][new_y] == 0:
                continue
            # check road
            if graph[new_x][new_y] == 1:
                graph[new_x][new_y] = graph[x][y] + 1
                q.append((new_x, new_y))
    return graph[row - 1][col - 1]

print(bfs(0, 0))


