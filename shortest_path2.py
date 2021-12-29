import heapq

INF = int(1e9)
node_count, edge_count, start_node = map(int, input().split())
graph = [[] for i in range(node_count + 1)]
distance = [INF] * (node_count + 1)

# get graph data
for _ in range(edge_count):
    st, en, cost = map(int, input().split())
    graph[st].append((en, cost))

def dijkstra(start_node):
    q = []
    heapq.heappush(q, (0, start_node))
    distance[start_node] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        # check neighbors
        for neigh in graph[node]:
            cost = dist + neigh[1]
        if cost < distance[neigh[0]]:
            distance[neigh[0]] = cost
            heapq.heappush(q, (cost, neigh[0]))

dijkstra(start_node)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count-1, max_distance)

