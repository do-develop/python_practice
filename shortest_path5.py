# dijkstra shortest path

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# for each tc (test case from input)
for tc in range(int(input())):
    node = int(input())
    graph = []
    for i in range(node):
        graph.append(list(map(int,input().split())))

distance = [[INF] * node for _ in range(node)]

x, y = 0, 0
q = [(graph[x][y], x, y)]
distance[x][y] = graph[x][y]

while q:
    dist, x, y = heapq.heappop(q)
    # if already processed, ignore
    if distance[x][y] < dist:
        continue
    # check adjacent nodes
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # check bounds
        if nx < 0 or nx >= node or ny < 0 or ny >= node:
            continue
        cost = dist + graph[nx][ny]
        if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q, (cost, nx, ny))

print(distance[node-1][node-1])
