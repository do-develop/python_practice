func maximumJumps(nums []int, target int) int {
    N := len(nums)
    dp := make([]int, N)

    for i := 1; i < N; i++ {
        dp[i] = -1
        for j := 0; j < i; j++ {
            if abs(nums[i] - nums[j]) <= target && dp[j] >= 0 {
                dp[i] = max(dp[i], dp[j] + 1)
            }
        }
    }
    return dp[N - 1]
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}