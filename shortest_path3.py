#floyd-warshall
INF = int(1e9)

node = int(input())
line = int(input())
# 2d list
graph = [[INF]*(node + 1) for _ in range(node + 1)]

#self to self costs 0
for a in range(1, node + 1):
    for b in range(1, node + 1):
        if a == b:
            graph[a][b] = 0

#get line info and intialise the value
for _ in range(line):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

#perform floyd-warshall algorithm
for k in range(1, node + 1):
    for a in range(1, node + 1):
        for b in range(1, node + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#print the result
for a in range(1, node + 1):
    for b in range(1, node + 1):
        if graph[a][b] == INF:
            print(0, end = " ")
        else:
            print(graph[a][b], end = " ")
    print()
