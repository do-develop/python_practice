func canPartitionGrid(grid [][]int) bool {
    R, C := len(grid), len(grid[0])
    sum := make([][]int64, R + 1)
    for i := range sum {
        sum[i] = make([]int64, C + 1)
    }

    var total int64 = 0
    for r := 0; r < R; r++ {
        for c := 0; c < C; c++ {
            sum[r+1][c+1] = sum[r+1][c] + sum[r][c+1] - sum[r][c] + int64(grid[r][c])
            total += int64(grid[r][c])
        }
    }

    for r := 0; r < R - 1; r++ {
        if total == sum[r+1][C] * 2 {
            return true
        }
    }

    for c := 0; c < C - 1; c++ {
        if total == sum[R][c+1] * 2 {
            return true
        }
    }
    return false
}