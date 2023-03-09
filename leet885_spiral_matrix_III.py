# time limit exceeded but more intuitive
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        path = [(rStart, cStart)]
        is_valid = lambda row, col: row >= 0 and row < rows and col >= 0 and col < cols
        
        steps = 1
        r, c = rStart, cStart
        while len(path) < rows * cols:
            # go right
            for step in range(steps):
                r, c = r, c + 1
                if is_valid(r, c):
                    path.append((r, c))
            
            # go down
            for step in range(steps):
                r, c = r + 1, c
                if is_valid(r, c):
                    path.append((r, c))
            
            # spiral point increase step
            steps += 1

            # go left
            for step in range(steps):
                r, c = r, c - 1
                if is_valid(r, c):
                    path.append((r, c))
            
            # go up
            for step in range(steps):
                r, c = r + 1, c
                if is_valid(r, c):
                    path.append((r, c))

            steps += 1
        return path


# final solution
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        path = []
        dx, dy, steps = 0, 1, 0
        x, y = rStart, cStart
        while len(path) < rows * cols:
            for _ in range(steps // 2 + 1):
                if 0 <= x < rows and 0 <= y < cols:
                    path.append([x, y])
                x, y = x + dx, y + dy
            dx, dy, steps = dy, -dx, steps + 1
        return path
