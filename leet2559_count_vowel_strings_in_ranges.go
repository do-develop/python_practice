func vowelStrings(words []string, queries [][]int) []int {
    prefixSum := make([]int, len(words) + 1)
    for i := 1; i <= len(words); i++ {
        prefixSum[i] = prefixSum[i - 1]
        if isVowelString(words[i-1]) {
            prefixSum[i]++
        }
    }

    result := make([]int, len(queries))
    for i, query := range queries {
        result[i] = prefixSum[query[1] + 1] - prefixSum[query[0]]
    }
    return result
}

func isVowelString(word string) bool {
    vowels := "aeiou"
    return strings.ContainsRune(vowels, rune(word[0])) && strings.ContainsRune(vowels, rune(word[len(word) - 1]))
}