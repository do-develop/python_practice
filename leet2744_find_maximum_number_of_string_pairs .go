func maximumNumberOfStringPairs(words []string) int {
    count := 0
    wordExist := make(map[string]bool)

    for _, w := range words {
        reversed := fmt.Sprintf("%c%c", w[1], w[0])
        if wordExist[reversed] {
            count++
        } else {
            wordExist[w] = true
        }
    }
    return count
}