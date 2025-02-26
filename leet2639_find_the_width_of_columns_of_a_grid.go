func findColumnWidth(grid [][]int) []int {
    widths := make([]int, len(grid[0]))

    for _, row := range grid {
        for colIdx, val := range row {
            valLen := len(strconv.Itoa(val))
            if widths[colIdx] < valLen {
                widths[colIdx] = valLen
            }
        }
    }
    return widths
}