func removeAlmostEqualCharacters(word string) int {
    var toBeChanged int

    for i := 1; i < len(word); i++ {
        if (word[i] >= word[i-1]) && (word[i] - word[i-1] <= 1) {
            toBeChanged++
            i++
        } else if (word[i] <= word[i-1]) && (word[i-1] - word[i] <= 1) {
            toBeChanged++
            i++
        }
    }
    return toBeChanged
}