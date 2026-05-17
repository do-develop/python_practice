func longestPalindromicSubsequence(s string, k int) int {
    N := len(s)
    
    // dp[i][j][k] = longest palindromic subsequence in s[i..j], using at most k operations
    dp := make([][][]int, N)
    for i := range dp {
        dp[i] = make([][]int, N)
        for j := range dp[i] {
            dp[i][j] = make([]int, k+1)
        }
    }

    // base case, single characters
    for i := 0; i < N; i++ {
        for x := 0; x <= k; x++ {
            dp[i][i][x] = 1
        }
    }

    // Fill by increasing interval length
    for length := 2; length <= N; length++ {
        for i := 0; i <= N - length; i++ {
            j := i + length - 1

            for x := 0; x <= k ; x++ {
                // Option 1: skip left or right end
                best := max(dp[i+1][j][x], dp[i][j-1][x])

                // Option 2: match s[i] and s[j] if affordable
                diff := abs(int(s[i]) - int(s[j]))
                cost := min(diff, 26-diff)
                if cost <= x {
                    inner := 0
                    if i + 1 <= j - 1 {
                        // reduce the cost
                        inner = dp[i+1][j-1][x-cost]
                    }
                    best = max(best, 2 + inner)
                }

                dp[i][j][x] = best
            }
        }
    }
    return dp[0][N-1][k]
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}