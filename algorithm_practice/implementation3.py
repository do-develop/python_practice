# 8 x 8 size (row  1 2 3 4 5 6 7 8, col a b c d e f g h)
# Get the knight location
location = input()
row = int(location[1])
col = int(ord(location[0])) - int(ord('a')) + 1  # ord() method converts a character into its Unicode code

# all possible 8 moves
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

# count possible moves
count = 0
for move in moves:
    next_row = row + move[0]
    next_col = col + move[1]

    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        count += 1

print(count)
"""
input = c2
output = 6
"""