func findTheLongestBalancedSubstring(s string) int {
    var N, longest int = len(s), 0
    for i := 0; i < N; {
        var zero, one int = 0, 0 // reset every start
        for i < N && s[i] == '0' {
            zero++
            i++
        }
        for i < N && s[i] == '1' {
            one++
            i++
        }
        longest = max(longest, -2 * max(-zero, -one))
    }
    return longest
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}