from collections import deque

for tc in range(int(input())):
    node = int(input())
    indegree = [0] * (node + 1)
    graph = [[False] * (node + 1) for i in range(node + 1)]

    # get last year ranks
    data = list(map(int, input().split()))
    for i in range(node):
        for j in range(i + 1, node):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    # get changed rank info this year
    changed = int(input())
    for i in range(changed):
        a, b = map(int, input().split())
        # change edge direction
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # topolgy sort
    result = []
    q = deque()

    for i in range(1, node + 1):
        if indegree[i] == 0:
            q. append(i)

    only = True     # only one result
    cycle = False   # cycle in the graph

    for i in range(node):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            only = False
            break

        now = q.popleft()
        result.append(now)

        for j in range(1, node + 1):
            if graph[now][j]:
                indegree[j] -= 1

                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not only:
        print("?")
    else:
        for i in result:
            print(i, end = ' ')
        print()

    
"""
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3



5 3 2 4 1 
2 3 1 
IMPOSSIBLE
"""
