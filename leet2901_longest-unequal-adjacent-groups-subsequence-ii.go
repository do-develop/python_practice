func getWordsInLongestSubsequence(words []string, groups []int) []string {
    N := len(groups)
    dp := make([]int, N) // longest subsequence length ending at index i so far
    prev := make([]int, N) // record the index of the previous index in the longest subsequence ending at i
    for i := range dp {
        dp[i] = 1 
        prev[i] = -1
    }
    maxIdx := 0

    for i := 1; i < N; i++ {
        for j := 0; j < i; j++ {
            // Appending words[i] to the sequence ending at words[j] makes a longer sequence: dp[j]+1 > dp[i]
            if check(words[i], words[j]) && groups[i] != groups[j] && dp[j] + 1 > dp[i] {
                dp[i] = dp[j] + 1
                prev[i] = j
            }
        }
        if dp[i] > dp[maxIdx] {
            maxIdx = i
        }
    }

    ans := []string{}
    for i := maxIdx; i >= 0; i = prev[i] {
        ans = append(ans, words[i])
    }
    reverse(ans)
    return ans
}

func check(s1, s2 string) bool {
    if len(s1) != len(s2) {
        return false
    }

    diff := 0
    for i := 0; i < len(s1); i++ {
        if s1[i] != s2[i] {
            diff++
            if diff > 1 {
                return false
            }
        }
    }
    return diff == 1
}

func reverse (arr []string) {
    for i, j := 0, len(arr) - 1; i < j; i, j = i + 1, j - 1 {
        arr[i], arr[j] = arr[j], arr[i]
    }
}