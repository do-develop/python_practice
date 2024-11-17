func longestContinuousSubstring(s string) int {
    N := len(s)

    ans, cnt := 1, 1

    for i := 1; i < N; i++ {
        if s[i] - s[i-1] == 1 {
            cnt++;
        } else {
            cnt = 1
        }
        ans = max(ans, cnt)
    }
    return ans
}