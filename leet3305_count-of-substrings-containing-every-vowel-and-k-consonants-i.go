func countOfSubstrings(word string, k int) int {
    count := 0
    N := len(word)

    for i := 0; i < N; i++ {
        consonants := 0
        vowels := map[byte]int{}
        for j := i; j < N; j++ {
            if word[j] == 'a' || word[j] == 'e' || word[j] == 'i' || word[j] == 'o' || word[j] == 'u' {
                vowels[word[j]]++
            } else {
                consonants++
            }
            if len(vowels) == 5 && consonants == k {
                count++
            }
        }
    }
    return count
}