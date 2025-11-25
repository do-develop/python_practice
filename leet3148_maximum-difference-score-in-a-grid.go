func maxScore(grid [][]int) int {
    rows, cols := len(grid), len(grid[0])
    dp := make([][]int, rows)
    for i := range rows {
        dp[i] = make([]int, cols)
    }

    score := math.MinInt

    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            currMin := math.MaxInt
            if indexIn(grid, r - 1, c) {
                currMin = min(currMin, dp[r - 1][c])
            }
            if indexIn(grid, r, c - 1) {
                currMin = min(currMin, dp[r][c - 1])
            }
            score = max(score, grid[r][c] - currMin)
            dp[r][c] = min(currMin, grid[r][c])
        }
    }
    return score
}

func indexIn[T any](mat[][]T, i, j int) bool {
    return i >= 0 && i < len(mat) && j >= 0 && j < len(mat[0])
}