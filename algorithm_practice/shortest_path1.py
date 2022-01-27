INF = int(1e9)
node_count, edge_count = map(int, input().split())
graph = [[INF] * (node_count + 1) for _ in range(node_count + 1)]

for a in range(1, node_count + 1):
    for b in range(1, node_count + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(edge_count):
    st, en = map(int, input().split())
    graph[st][en] = 1
    graph[en][st] = 1

stop, destination = map(int, input().split())

for k in range(1, node_count+1):
    for a in range(1, node_count+1):
        for b in range(1, node_count+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][stop] + graph[stop][destination]

if distance >= INF:
    print("-1")
else:
    print(distance)