func specialGrid(n int) [][]int {
    size := 1 << n // 2^n
    grid := make([][]int, size)
    for i := range grid {
        grid[i] = make([]int, size)
    }

    var fill func(row, col, size, start int)
    fill = func(row, col, size, start int) {
        if size == 1 {
            grid[row][col] = start
            return
        }

        half := size / 2
        quadrantSize := half * half // number of cells in each quadrant
        // Order: top-right → bottom-right → bottom-left → top-left
        fill(row, col+half, half, start)
        fill(row+half, col+half, half, start + quadrantSize)
        fill(row+half, col, half, start + quadrantSize * 2)
        fill(row, col, half, start + quadrantSize * 3)
    }

    fill(0, 0, size, 0)
    return grid
}