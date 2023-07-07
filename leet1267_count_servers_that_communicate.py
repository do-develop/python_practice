class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # total - count of isolated servers
        rows = [0] * len(grid)
        cols = [0] * len(grid[0])

        total = isolated = 0

        # first iteration - update rows, cols array and total count
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1
                    total += 1
        # second iteration - get the isolated server count
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == 1:
                    if rows[r] == 1 and cols[c] == 1: # isolated?
                        isolated += 1
        
        return total - isolated
