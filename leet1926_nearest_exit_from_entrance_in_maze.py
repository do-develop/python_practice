class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # BFS - approach 1
        '''
        rows, cols = len(maze), len(maze[0])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        q = deque([entrance])

        # using extra space to keep track of the visited positions
        visited = {tuple(entrance)}
        steps = 0

        while q:
            for _ in range(len(q)):
                xo, yo = q.popleft()
                if (0 in [xo, yo] or xo==rows-1 or yo==cols-1) and [xo,yo] != entrance:
                    return steps
                for xn, yn in directions:
                    x, y = xo + xn, yo + yn
                    if 0 <= x < rows and 0 <= y < cols and maze[x][y] == '.' and (x, y) not in visited:
                        visited.add((x, y))
                        q.append((x, y))
            steps += 1
        return -1
        '''
        # BFS - approach 2
        rows, cols = len(maze), len(maze[0])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        q = deque([[entrance[0], entrance[1], 0]])
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            xo, yo, steps = q.popleft()
            if (0 in [xo, yo] or xo == rows-1 or yo == cols-1) and [xo, yo] != entrance:
                return steps
            for xn, yn in directions:
                x, y = xo + xn, yo + yn
                if 0 <= x < rows and 0 <= y < cols and maze[x][y] == '.':
                    maze[x][y] = '+'
                    q.append([x, y, steps + 1])
        return -1
