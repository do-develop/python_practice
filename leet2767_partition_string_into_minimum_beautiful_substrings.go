func minimumBeautifulSubstrings(s string) int {
    N := len(s)
    dp := make([]int, N + 1)

    for i := range dp {
        dp[i] = math.MaxInt32
    }
    dp[0] = 0

    for i := 1; i <= N; i++ {
        for j := 0; j < i; j++ {
            if isBeautiful(s[j:i]) {
                dp[i] = min(dp[i], dp[j] + 1)
            }
        }
    }

    if dp[N] == math.MaxInt32 {
        return -1
    }
    return dp[N]
}

func isBeautiful(s string) bool {
    if len(s) == 0 || s[0] == '0' {
        return false
    }

    num, err := strconv.ParseInt(s, 2, 64)
    if err != nil {
        return false
    }

    for num > 1 {
        if num % 5 != 0 {
            return false
        }
        num /= 5
    }
    return true
}

