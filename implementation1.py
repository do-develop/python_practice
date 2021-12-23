# size x size array, get size
size = int(input())
# initial coordinate
x, y = 1, 1
plans = input().split()

# direction for each plans, L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            new_x = x + dx[i]
            new_y = y + dy[i]
    # if the coordinate is out of bounds, ignore (do not update coordinate)
    if new_x < 1 or new_y < 1 or new_x > size or new_y > size:
        continue
    # update the coordinate
    x, y = new_x, new_y

print(x, y)

"""
5
R R R U D D
result = 3, 4
"""


