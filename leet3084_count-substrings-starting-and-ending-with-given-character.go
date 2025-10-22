func countSubstrings(s string, c byte) int64 {
    var count int64

    for i := 0; i < len(s); i++ {
        if c == s[i] {
            count++
        }
    }

    return count * (count + 1) / 2
}