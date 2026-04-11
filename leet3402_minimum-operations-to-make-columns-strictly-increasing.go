func minimumOperations(grid [][]int) int {
    ops := 0

    for r := 1; r < len(grid); r++ {
        for c := 0; c < len(grid[0]); c++ {
            if grid[r][c] <= grid[r-1][c] {
                value := grid[r-1][c] - grid[r][c] + 1
                ops += value
                grid[r][c] += value
            }
        }
    }
    return ops
}