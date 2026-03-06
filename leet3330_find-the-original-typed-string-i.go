func possibleStringCount(word string) int {
    N, count := len(word), 1
    for i := 1; i < N; i++ {
        if word[i - 1] == word[i] {
            count++
        }
    }
    return count
}