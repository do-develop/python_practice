# Kruskal Algorithm

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

node, edge = map(int, input().split())
parent = [0] * (node + 1)

graph = []
connect_cost = 0

for i in range(1, node+1):
    parent[i] = i

for _ in range(edge):
    x, y, cost = map(int, input().split())
    graph.append((cost, x, y))

# sort by the cost
graph.sort()
total_cost = 0

for e in graph: # for each edge
    cost, a, b = e
    total_cost += cost

    # if no cycle then add
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        connect_cost += cost

print(total_cost - connect_cost)


"""
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11

51
"""
