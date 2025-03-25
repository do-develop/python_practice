func differenceOfDistinctValues(grid [][]int) [][]int {
    ROWS, COLS := len(grid), len(grid[0])
    res := make([][]int, ROWS)

    for i := range res {
        res[i] = make([]int, COLS)
    }
    for r := 0; r < ROWS; r++ {
        for c := 0; c < COLS; c++ {
            topLeft, bottomRight := make(map[int]bool), make(map[int]bool)
            getTopLeft(grid, r - 1, c - 1, topLeft)
            getBottomRight(grid, r + 1, c + 1, bottomRight)
            res[r][c] = abs(len(topLeft) - len(bottomRight))
        }
    }
    return res
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func getTopLeft(grid[][]int, r, c int, count map[int]bool){
    if r < 0 || r >= len(grid) || c < 0 || c >= len(grid[0]) {return}
    count[grid[r][c]] = true
    getTopLeft(grid, r - 1, c - 1, count)
}

func getBottomRight(grid[][]int, r, c int, count map[int]bool) {
    if r < 0 || r >= len(grid) || c < 0 || c >= len(grid[0]) {return}
    count[grid[r][c]] = true
    getBottomRight(grid, r + 1, c + 1, count)
}