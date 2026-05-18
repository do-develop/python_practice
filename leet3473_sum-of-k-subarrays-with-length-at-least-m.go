func maxSum(nums []int, k int, m int) int {
    N := len(nums)

    prefix := make([]int, N + 1)
    for i, v := range nums {
        prefix[i+1] = prefix[i] + v
    }

    //dp[i][j] = nums[0..i-1] 에서 j개의 부분배열을 골랐을 때 최대합
    dp := make([][]int, N+1)
    for i := range dp {
        dp[i] = make([]int, k+1)
        for j := range dp[i] {
            dp[i][j] = math.MinInt32
        }
    }

    // base case
    for i := 0; i <= N; i++ {
        dp[i][0] = 0
    }

    for j := 1; j <= k; j++ {
        best := math.MinInt32

        for i := 1; i <= N; i++ {
            start := i - m
            if start >= 0 && dp[start][j-1] != math.MinInt32 {
                best = max(best, dp[start][j-1]-prefix[start])
            }

            // option 1: no i-th item
            dp[i][j] = dp[i-1][j]

            // option 2: end with i-th item
            if best != math.MinInt32 {
                dp[i][j] = max(dp[i][j], prefix[i] + best)
            }
        }
    }
    return dp[N][k]
}