func maximumAmount(coins [][]int) int {
    rows, cols := len(coins), len(coins[0])

    // dynamic progamming approach
    const NEG_INF = math.MinInt32/2
    dp := make([][][3]int, rows)
    for r := range dp {
        dp[r] = make([][3]int, cols)
        for c := range dp[r] {
            dp[r][c] = [3]int{NEG_INF, NEG_INF, NEG_INF}
        }
    }

    // Base case: starting cell
    dp[0][0][0] = coins[0][0]
    if coins[0][0] < 0 {
        dp[0][0][1] = 0 // neutralised
    }

    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            if r == 0 && c == 0 {
                continue
            }
            for k := 0; k <=2; k++ {
                prev := NEG_INF
                if r > 0 && dp[r-1][c][k] != NEG_INF {
                    prev = max(prev, dp[r-1][c][k])
                }
                if c > 0 && dp[r][c-1][k] != NEG_INF {
                    prev = max(prev, dp[r][c-1][k])
                }
                if prev == NEG_INF {
                    continue
                }

                // case 1: take the cell as-is
                dp[r][c][k] = max(dp[r][c][k], prev + coins[r][c])
                // case 2: neautralize the robber cell
                if coins[r][c] < 0 && k < 2 {
                    dp[r][c][k+1] = max(dp[r][c][k+1], prev)
                }
            }
        }
    }

    best := NEG_INF
    for k := 0; k <= 2; k++ {
        best = max(best, dp[rows-1][cols-1][k])
    }
    return best
}