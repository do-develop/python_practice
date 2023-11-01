class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # recursive approach
        rows, cols = len(grid), len(grid[0])
        def col_get_out(r, c):
            # reach the end and got out
            if r == rows:
                return c
            
            new_col = c + grid[r][c]
            # check stuck condition
            if(
                new_col == -1 
                or new_col == cols
                or grid[r][new_col] != grid[r][c]  # stuck at \/
            ):
                return -1
            return col_get_out(r + 1, new_col)
        
        answer = []
        for c in range(cols):
            answer.append(col_get_out(0, c))
        return answer
