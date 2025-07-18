func shortestBeautifulSubstring(s string, k int) string {
    var shortest string
    var l, freq int

    for r := range s {
        if s[r] == '1' {
            freq++
        }
        for freq == k {
            substr := s[l:r + 1]
            if shortest == "" || (len(substr) < len(shortest)) || (len(substr) == len(shortest) && substr < shortest) {
                shortest = substr
            }

            if s[l] == '1' {
                freq--
            }
            l++
        }
    }
    return shortest
}