"""
acmicpc.net/problem/14502
"""

row, col = map(int, input().split())
map_data = []
after_wall = [[0] * col for _ in range(row)]

for _ in range(row):
    map_data.append(list(map(int, input().split())))

# move direction 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS to spread the virus
def spread_virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # condition that the virus can spread
        if 0 <= nx < row and 0 <= ny < col:
            if after_wall[nx][ny] == 0:
                after_wall[nx][ny] = 2
                spread_virus(nx, ny)

def get_score():
    score = 0
    for i in range(row):
        for j in range(col):
            if after_wall[i][j] == 0:
                score += 1
    return score

# DFS to calculate every possible wall installation and following scores
def dfs(wall_count):
    global result
    # base case
    if wall_count == 3:
        for i in range(row):
            for j in range(col):
                after_wall[i][j] = map_data[i][j]

        for i in range(row):
            for j in range(col):
                if after_wall[i][j] == 2:
                    spread_virus(i, j)
        result = max(result, get_score())
        return
    # install walls in an empty space
    for i in range(row):
        for j in range(col):
            if map_data[i][j] == 0:
                map_data[i][j] = 1
                wall_count += 1
                dfs(wall_count)
                map_data[i][j] = 0
                wall_count -= 1

dfs(0)
print(result)
    
        
        
            
