import heapq
INF = int(1e9)

node, edge = map(int, input().split())
start = 1  # start node
graph = [[] for i in range(node + 1)]
distance = [INF] * (node + 1)

# get edge info
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# perform dijkstra
dijkstra(start)

far_node = 0
far_dist = 0
result = []

for i in range(1, node+1):
    if far_dist < distance[i]:
        far_node = i
        far_dist = distance[i]
        result = [far_node]
    elif far_dist == distance[i]:
        result.append(i)

print(far_node, far_dist, len(result))
    
            
