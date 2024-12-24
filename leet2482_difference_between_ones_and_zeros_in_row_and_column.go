func onesMinusZeros(grid [][]int) [][]int {
    N, M := len(grid), len(grid[0])
    row := make([]int, N)
    col := make([]int, M)

    for r := 0; r < N; r++ {
        for c := 0; c < M; c ++ {
            if grid[r][c] == 1 {
                row[r]++
                col[c]++
            }
        }
    }

    diff := make([][]int, N)
    for i := range diff {
        diff[i] = make([]int, M)
    }
    for r := 0; r < N; r++ {
        for c := 0; c < M; c++ {
            diff[r][c] = 2 * (row[r] + col[c]) - N - M
        }
    }
    
    return diff
}