func countPrefixSuffixPairs(words []string) int {
    N := len(words)
    count := 0

    for i := 0; i < N - 1; i++ {
        for j := i + 1; j < N; j++ {
            if isPrefixAndSuffix(words[i], words[j]) {
                count++
            }
        }
    }
    return count
}

func isPrefixAndSuffix(x, y string) bool {
    if len(x) > len(y) {
        return false
    }
    return strings.HasPrefix(y, x) && strings.HasSuffix(y, x)
}