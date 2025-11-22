var frequencies = make([]int, 'z'+1)
var dp = make([]int, 1e3+1)

func minimumSubstringsInPartition(s string) int {
    N := len(s)
    dp[0] = 0

    for end := 1; end <= N; end++ {
        clear(frequencies)

        dp[end] = dp[end - 1] + 1
        maxFreq, distinct := 0, 0

        for start := end; start > 0; start-- {
            ch := s[start - 1]

            if frequencies[ch] == 0 {
                distinct++
            }

            frequencies[ch]++
            maxFreq = max(maxFreq, frequencies[ch])

            if end - start + 1 == maxFreq * distinct {
                dp[end] = min(dp[end], dp[start - 1] + 1)
            }
        }
    }
    return dp[N]
}