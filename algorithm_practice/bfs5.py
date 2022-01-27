from collections import deque
INF = 1e9

map_size = int(input())
map_data= []
for i in range(map_size):
    map_data.append(list(map(int, input().split())))

now_size = 2
now_x, now_y = 0, 0

for i in range(map_size):
    for j in range(map_size):
        if map_data[i][j] == 9:
            now_x, now_y = i, j
            map_data[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# calculate shortest path using bfs
def bfs():
    dist = [[-1] * map_size for _ in range(map_size)]
    q = deque([(now_x, now_y)]) # insert start position
    dist[now_x][now_y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < map_size and 0 <= ny < map_size:
                if dist[nx][ny] == -1 and map_data[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

# with shortest path data, find the fish to eat
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(map_size):
        for j in range(map_size):
            if dist[i][j] != -1 and 1 <= map_data[i][j] < now_size:
                if dist[i][j] < min_dist:
                    x,y = i,j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist

result_dist = 0
ate = 0

while True:
    prey = find(bfs())
    if prey == None:
        print(result_dist)
        break
    else:
        now_x, now_y = prey[0], prey[1]
        result_dist += prey[2]
        map_data[now_x][now_y] = 0
        ate += 1

        if ate >= now_size:
            now_size += 1
            ate = 0
            
    
        
