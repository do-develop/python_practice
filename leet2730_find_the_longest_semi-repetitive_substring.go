func longestSemiRepetitiveSubstring(s string) int {
    l, r := 0, 1
    count := 0
    longest := 1

    for ; r < len(s); r++ {
        if s[r - 1] == s[r] {
            count++
        } 
        for ; count > 1; l++ {
            if s[l] == s[l + 1] {
                count--
            }
        }
        if longest < (r - l + 1) {
            longest = (r - l + 1)
        }
    }
    return longest
}