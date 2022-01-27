INF = int(1e9)

node, edge = map(int, input().split())
graph = [[INF] * (node + 1) for _ in range(node + 1)]

# self to self costs 0
for a in range(1, node + 1):
    for b in range(1, node + 1):
        if a == b:
            graph[a][b] = 0

# get edge info
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a][b] = 1

# use floyd-warshll algorithm
for k in range(1, node + 1):
    for a in range(1, node + 1):
        for b in range(1, node + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


result = 0
# check if reachable
for i in range(1, node + 1):
    count = 0
    for j in range(1, node + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1

        if count == node:
            result += 1

print(result)
