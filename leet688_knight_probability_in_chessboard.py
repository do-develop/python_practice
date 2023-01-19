class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        memo = {}
        moves = ((1, 2), (-1, 2), (1, -2), (-1, -2),
                 (2, 1), (-2, 1), (2, -1), (-2, -1))
        
        def dfs(x, y, p, step):
            prb = 0 # probability
            if 0 <= x < n and 0 <= y < n: # within bound
                if step < k:
                    for dx, dy in moves:
                        x_next, y_next = x + dx, y + dy
                        if (x_next, y_next, step + 1) not in memo:
                            memo[(x_next, y_next, step + 1)] = dfs(x_next, y_next, p/8, step + 1)
                        prb += memo[(x_next, y_next, step + 1)] 
                else: # last move (kth move)
                    prb = p
            return prb
        return dfs(row, column, 1, 0)
