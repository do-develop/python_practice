"""
acmicpc.net/problem/18405
"""

from collections import deque

size, types = map(int, input().split())
board = []
virus_data = []

for i in range(size):
    board.append(list(map(int, input().split())))
    for j in range(size):
        if board[i][j] != 0:
            # insert virus type, time, x coord, y coord
            virus_data.append((board[i][j], 0, i, j))

# sort and move to queue (because the low number virus spread first)
virus_data.sort()
q = deque(virus_data)

target_sec, target_x, target_y = map(int, input().split())

# virus spreads in 4 directions
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS
while q:
    virus, sec, x, y = q.popleft()
    if sec == target_sec:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < size and 0 <= ny < size:
            if board[nx][ny] == 0:
                board[nx][ny] = virus
                q.append((virus, sec + 1, nx, ny))

print(board[target_x - 1][target_y - 1])
