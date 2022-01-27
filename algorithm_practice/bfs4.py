from collections import deque

size, diff_min, diff_max = map(int, input().split())

graph = []
for _ in range(size):
    graph.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def process(x, y, index):
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))
    visited[x][y] = index
    population = graph[x][y]
    country_count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < size and 0 <= ny < size and visited[nx][ny] == -1:
                if diff_min <= abs(graph[nx][ny] - graph[x][y]) <= diff_max:
                    q.append((nx, ny))
                    visited[nx][ny] = index
                    population += graph[nx][ny]
                    country_count += 1
                    united.append((nx, ny))

    # divide populations
    for i, j in united:
        graph[i][j] = population // country_count
        
    return country_count

move_count = 0

while True:
    visited = [[-1] * size for _ in range(size)]
    index = 0
    for i in range(size):
        for j in range(size):
            if visited[i][j] == -1:  # not visited
                process(i, j, index)
                index += 1

    if index == size * size:
        break
    move_count += 1

print(move_count)
