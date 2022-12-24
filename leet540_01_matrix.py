# BFS approach
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        output = [[-1] * len(mat[0]) for _ in range(len(mat))]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    q.append((r, c, 0))
                    output[r][c] = 0
        # bfs
        visited = set()
        while q:
            r, c, depth = q.popleft()
            if (r, c) in visited:
                continue
            visited.add((r,c))
            output[r][c] = depth
            # if in bounds
            if r > 0 and (r - 1, c) not in visited:
                q.append((r - 1, c, depth + 1))
            if r + 1 < len(mat) and (r + 1, c) not in visited:
                q.append((r + 1, c, depth + 1))
            if c > 0 and (r, c - 1) not in visited:
                q.append((r, c - 1, depth + 1))
            if c + 1 < len(mat[0]) and (r, c + 1) not in visited:
                q.append((r, c + 1, depth + 1))
        return output
