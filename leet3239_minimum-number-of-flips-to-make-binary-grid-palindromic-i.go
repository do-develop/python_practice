func minFlips(grid [][]int) int {
    var flipRow, flipCol int

    for r := 0; r < len(grid); r++ {
        for c := 0; c < len(grid[r])/2; c++ {
            if grid[r][c] != grid[r][len(grid[r]) - 1 - c] {
                flipRow++
            }
        } 
    }

    for c := 0; c < len(grid[0]); c++ {
        for r := 0; r < len(grid)/2; r++ {
            if grid[r][c] != grid[len(grid) - 1 - r][c] {
                flipCol++
            }
        }
    }

    return min(flipRow, flipCol)
}