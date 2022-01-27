row, col = map(int, input().split())

# get 2-D list
graph = []
for i in range(row):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= row or y <= -1 or y >= col:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

count = 0
for r in range(row):
    for c in range(col):
        if dfs(r, c) == True:
            count += 1

print(count)