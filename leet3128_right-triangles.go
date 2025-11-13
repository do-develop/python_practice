func numberOfRightTriangles(grid [][]int) int64 {
    rows, cols := len(grid), len(grid[0])

    rowCounts := make([]int, rows)
    colCounts := make([]int, cols)

    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            if grid[r][c] == 1 {
                rowCounts[r]++
                colCounts[c]++
            }
        }
    }

    triangles := 0

    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            if grid[r][c] == 1 {
                triangles += (rowCounts[r] - 1) * (colCounts[c] - 1)
            }
        }
    }
    return int64(triangles)
}