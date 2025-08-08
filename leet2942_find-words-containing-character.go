func findWordsContaining(words []string, x byte) []int {
    indices := [] int{}
    N := len(words)

    for i := 0; i < N; i++ {
        for j := 0; j < len(words[i]); j++ {
            if words[i][j] == x {
                indices = append(indices, i)
                break
            }
        }
    }
    return indices
}