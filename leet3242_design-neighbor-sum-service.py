class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.size = len(grid)
        self.positions = [None] * self.size ** 2
        for r, c in product(range(self.size), range(self.size)):
            self.positions[grid[r][c]] = r, c 

    def adjacentSum(self, value: int) -> int:
        r, c = self.positions[value]
        total = 0
        total += self.grid[r-1][c] if r >= 1 else 0 
        total += self.grid[r+1][c] if r + 1 < self.size else 0
        total += self.grid[r][c-1] if c >= 1 else 0
        total += self.grid[r][c+1] if c + 1 < self.size else 0
        return total
        

    def diagonalSum(self, value: int) -> int:
        r, c = self.positions[value]
        total = 0
        total += self.grid[r-1][c-1] if r >= 1 and c >= 1 else 0 
        total += self.grid[r+1][c+1] if r + 1 < self.size and c + 1 < self.size else 0
        total += self.grid[r+1][c-1] if r + 1 < self.size and c >= 1 else 0
        total += self.grid[r-1][c+1] if r >= 1 and c + 1 < self.size else 0
        return total

        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
