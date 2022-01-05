from collections import deque

city_count, road_count, k_distance, start_city = map(int, input().split())
graph = [[] for _ in range(city_count + 1)]

for _ in range(road_count):
    a, b = map(int, input().split())
    graph[a].append(b)

distances = [-1] * (city_count + 1)
distances[start_city] = 0

# BFS
q = deque([start_city])
while q:
    now = q.popleft()
    for neighbor in graph[now]:
        if distances[neighbor] == -1:
            distances[neighbor] = distances[now] + 1
            q.append(neighbor)

# k distant city will be printed in the ascending order
check = False
for i in range(1, city_count + 1):
    if distances[i] == k_distance:
        print(i)
        check = True

if check == False:
    print(-1)
