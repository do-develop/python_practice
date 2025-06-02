func maximizeTheProfit(n int, offers [][]int) int {
    dp := make([]int, n + 1)
    m := make([][][]int, n + 1)

    // sort offers by their end day
    for _, offer := range offers {
        start := offer[0]
		m[start] = append(m[start], offer)
    }

    // forward DP to compute max profit
    for day := 1; day <= n; day++ {
        // Option 1: skip the day
        dp[day] = max(dp[day], dp[day - 1])

        // Option 2: take offers starting at day - 1
        for _, offer := range m[day-1] {
			end, gold := offer[1], offer[2]
			if end+1 <= n {
				dp[end+1] = max(dp[end+1], dp[day-1]+gold)
			}
		}
    }

    return dp[n]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}