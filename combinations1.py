from itertools import combinations

size = int(input())
board = []
teachers = []
spaces = []

for i in range(size):
    board.append(list(input().split()))
    for j in range(size):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))

def search(x, y, direction):
    # left search
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    # right search
    if direction == 1:
        while y < size:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    # upward search
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    # downward search
    if direction == 3:
        while x < size:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False

# check if a student can be found
def found_student():
    for x, y in teachers:
        for direction in range(4):
            if search(x, y, direction):
                return True
    return False

found_wall_combination = False
# check all combinations of intalling 3 walls
for comb in combinations(spaces, 3):
    # install walls
    for x, y in comb:
        board[x][y] = 'O'

    if not found_student():
        found_wall_combination = True
        break
    # remove walls
    for x, y in comb:
        board[x][y] = 'X'

if found_wall_combination:
    print("Yes, all students can hide from teachers")
else:
    print("No, it is not possible to hide from teachers")
