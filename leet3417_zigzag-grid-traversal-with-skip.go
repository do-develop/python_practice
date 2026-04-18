func zigzagTraversal(grid [][]int) []int {
    result := []int{}

    for r := 0; r < len(grid); r++ {
        if r % 2 == 1 {
            for c := len(grid[0]) - 1; c >= 0; c-- {
                if c % 2 == 1 {
                    result = append(result, grid[r][c])
                }
            }
        } else {
            for c := 0; c < len(grid[0]); c++ {
                if c % 2 == 0 {
                    result = append(result, grid[r][c])
                }
            }
        }
    }
    return result
}