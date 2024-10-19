func largestLocal(grid [][]int) [][]int {
    result := make([][]int, 0)
    R, C := len(grid), len(grid[0])

    for row := range R - 2 {
        localMaxRow := make([]int, 0)
        for col := range C - 2 {
            curr := grid[row][col]
            for x := range 3 {
                for y := range 3{
                    curr = max(curr, grid[row + x][col + y])
                }
            }
            localMaxRow = append(localMaxRow, curr)
        }
        result = append(result, localMaxRow)
    }
    return result
}