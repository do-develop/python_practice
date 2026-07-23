func minCost(m int, n int, waitCost [][]int) int64 {
    waitCost[0][0] = 0
    waitCost[m-1][n-1] = 0

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            prev := math.MaxInt64
            if i == 0 && j == 0 {
                prev = 0
            }
            if i > 0 && waitCost[i-1][j] < prev {
                prev = waitCost[i-1][j]
            }
            if j > 0 && waitCost[i][j-1] < prev {
                prev = waitCost[i][j-1]
            }
            waitCost[i][j] += (i + 1) * (j + 1) + prev
        }
    }
    return int64(waitCost[m-1][n-1])
}