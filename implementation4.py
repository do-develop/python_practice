# get size of the map
row, col = map(int, input().split())
# a variable to mark visited locations
visited = [[0] * col for _ in range(row)]
# get current location and direction
x, y, direction = map(int, input().split())
visited[x][y] = 1  # mark current position as visited

# get total map data
map_data = []
for i in range(row):
    map_data.append(list(map(int, input().split())))

# define directions (north, east, south, west)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# function to turn left
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# start the simulation
visit_count = 1
turn_time = 0
while True:
    turn_left()
    new_x = x + dx[direction]
    new_y = y + dy[direction]
    # after left turn, there is land that is not yet visited
    if map_data[new_x][new_y] == 0 and visited[new_x][new_y] == 0:
        visited[new_x][new_y] = 1
        x, y = new_x, new_y
        visit_count += 1
        turn_time = 0
        continue
    # after left turn, there is sea or visited land
    else:
        turn_time += 1
    # can't go any 4 directions
    if turn_time == 4:
        new_x = x - dx[direction]
        new_y = y - dy[direction]
        if map_data[new_x][new_y] == 0:
            x, y = new_x, new_y
        else:
            break
        turn_time = 0

print(visit_count)

"""
input:
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
output:
3
"""