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

node = int(input())
parent = [0] * (node + 1)
edges = []
min_cost = 0

for i in range(1, node + 1):
    parent[i] = i

x = []
y = []
z = []

for i in range(1, node + 1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

# process adjacent nodes
for i in range(node - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1] [1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1] [1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1] [1]))

# sort by costs
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a, b)
        min_cost += cost

print(min_cost)


"""
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19

4
"""
