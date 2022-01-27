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

student_count, operation_count = map(int, input().split())
parent = [0] * (student_count + 1)

for i in range(0, student_count + 1):
    parent[i] = i

for i in range(operation_count):
    oper, a, b = map(int, input().split())
    # union operation
    if oper == 0:
        union_parent(parent, a, b)
    # find operation
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("Same Team")
        else:
            print("Different Team")

