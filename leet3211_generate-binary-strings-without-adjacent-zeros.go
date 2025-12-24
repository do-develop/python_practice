func validStrings(n int) []string {
    ans := make([]string, 0, n * n)

    var f func(s string)
    f = func(s string) {
        if len(s) == n {
            ans = append(ans, s)
            return
        }
        if s[len(s) - 1] == '0' {
            f(s + "1")
        } else {
            f(s + "0")
            f(s + "1")
        }
    }
    f("1")
    f("0")
    return ans
}