# disjoint set

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# get user input
count, route = map(int, input().split())
parent = [0] * (count + 1)

for i in range(1, count + 1):
    parent[i] = i

# perfom union operation
for i in range(count):
    data = list(map(int, input().split()))
    for j in range(count):
        if data[j] == 1:  #it means i and j are connected
            union_parent(parent, i + 1, j + 1)

# get route plan
plan = list(map(int, input().split()))

result = True
for i in range(route - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False

# if all nodes in the route plan connected
if result:
    print("YES")
else:
    print("NO")



"""
TEST DATA
input:
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3

output:
YES
"""
