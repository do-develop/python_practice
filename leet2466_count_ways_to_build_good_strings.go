func countGoodStrings(low int, high int, zero int, one int) int {
    dp := make([]int, high + 1)
    dp[0] = 1
    res := 0

    for cur := 0; cur < high + 1;  cur++ {
        if cur + zero <= high {
            dp[cur + zero] += dp[cur]
            dp[cur + zero] %= 1000000007
        }
        if cur + one <= high {
            dp[cur + one] += dp[cur]
            dp[cur + one] %= 1000000007
        }
        if cur >= low {
            res += dp[cur]
        }
    }
    return res % 1000000007
}