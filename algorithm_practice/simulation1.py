board_size = int(input())
apple_count = int(input())
board = [[0] * (board_size + 1) for _ in range(board_size + 1)]
info = []  # direction switch will be recorded

for _ in range(apple_count):
    a, b = map(int, input().split())
    board[a][b] = 1

turn_count = int(input())
for _ in range(turn_count):
    sec, char = input().split()
    info.append((int(sec), char))  # tuple

# EAST, SOUTH, WEST, NORTH
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    board[x][y] = 2 # snake position is marked as 2
    direction = 0
    time = 0
    turn_index = 0
    q = [(x,y)]

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # check game ending condition
        if 1 <= nx <= board_size and 1 <= ny <= board_size and board[nx][ny] != 2:
            # check apple
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
            # no apple then remove the tail
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
        else:
            time += 1
            break
        x, y = nx, ny  # move to the next position
        time += 1
        if turn_index < 1 and time == info[turn_index][0]:
            direction = turn(direction, info[turn_index][1])
            turn_index += 1

    return time

print(simulate())
        
                
                
    
    
