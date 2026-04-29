func findValidPair(s string) string {
    counter := make(map[rune]int)
    for _, c := range s {
        counter[c]++
    }

    for i := 1; i < len(s); i++ {
        // only cares about the pairs
        if s[i] != s[i-1] && counter[rune(s[i])] == int(s[i]-'0') && counter[rune(s[i-1])] == int(s[i-1]-'0') {
            return s[i-1:i+1]
        }
    }
    return ""
}