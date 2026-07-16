func findCoins(numWays []int) []int {
    N := len(numWays)
    dp := make([]int64, N + 1)
    dp[0] = 1

    var coins []int

    for i := 1; i <= N; i++ {
        target := int64(numWays[i-1])
        diff := target - dp[i]

        switch {
            case diff == 0:
                continue
            case diff == 1:
                coins = append(coins, i)
                for j := i; j <= N; j++ {
                    dp[j] += dp[j-i]
                }
            default:
                return []int{}
        }
    }
    return coins
}