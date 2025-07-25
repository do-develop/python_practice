func lengthOfLongestSubsequence(nums []int, target int) int {
    dp := make([]int, target + 1)

    for i := range dp {
        dp[i] = -1 // target is not achievable
    }
    // base case
    dp[0] = 0
    for i := range nums {
        for j := target; j > 0; j-- {
            if (j - nums[i] >= 0) && (dp[j - nums[i]] != -1) {
                dp[j] = max(dp[j], dp[j - nums[i]] + 1)
            }
        }
    }
    return dp[target]
}

func max(x, y int) int {
    if x < y {
        return y
    }
    return x
}