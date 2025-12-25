func numberOfSubmatrices(grid [][]byte) int {
    rows, cols := len(grid), len(grid[0])
    res := 0
    X := make([][]int, rows + 1)
    Y := make([][]int, rows + 1)

    for i := range X {
        X[i] = make([]int, cols + 1)
        Y[i] = make([]int, cols + 1)
    }

    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            X[i+1][j+1] = X[i][j+1] + X[i+1][j] - X[i][j] + boolToInt(grid[i][j] == 'X')
            Y[i+1][j+1] = Y[i][j+1] + Y[i+1][j] - Y[i][j] + boolToInt(grid[i][j] == 'Y')
            if X[i+1][j+1] == Y[i+1][j+1] && X[i+1][j+1] > 0 {
                res++
            }
        }
    }
    return res
}

func boolToInt(b bool) int {
	if b {
		return 1
	}
	return 0
}