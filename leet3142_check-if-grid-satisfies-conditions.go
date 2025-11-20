func satisfiesConditions(grid [][]int) bool {
    rows, cols := len(grid), len(grid[0])

    if rows == 0 || cols == 0 {
        return true
    }

    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            if r < rows - 1 && grid[r][c] != grid[r + 1][c] {
                return false
            }
            if c < cols - 1 && grid[r][c] == grid[r][c + 1] {
                return false
            }
        }
    }
    return true
}