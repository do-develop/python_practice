class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        r = c = mx = d = 0
        move = [(0, 1), (-1, 0), (0, -1), (1, 0)] # north, west, south, east
        obstacles = set([(x, y) for x, y in obstacles])
        for command in commands:
            if command == -2:
                d = (d + 1) % 4
            elif command == -1:
                d = (d - 1) % 4
            else:
                x, y = move[d]
                while command and (r + x, c + y) not in obstacles:
                    r += x
                    c += y
                    command -= 1
            mx = max(mx, r ** 2 + c ** 2) # Euclidean distance
        return mx
