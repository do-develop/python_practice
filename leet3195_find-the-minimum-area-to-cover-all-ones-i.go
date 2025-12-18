func minimumArea(grid [][]int) int {
    rows, cols := len(grid), len(grid[0])
    minR, maxR := rows, 0
    minC, maxC := cols, 0

    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            if grid[r][c] == 1{
                minR = min(minR, r)
                maxR = max(maxR, r)
                minC = min(minC, c)
                maxC = max(maxC, c)
            }
        }
    }

    return (maxR - minR + 1) * (maxC - minC + 1)
}