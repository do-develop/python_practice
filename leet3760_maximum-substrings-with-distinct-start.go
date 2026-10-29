func maxDistinct(s string) int {
    counter := make(map[rune]bool)
    for _, ch := range s {
        counter[ch] = true
    }
    return len(counter)
}