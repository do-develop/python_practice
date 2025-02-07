func vowelStrings(words []string, left int, right int) int {
    vowels := "aeiou"
    count := 0

    for i := left; i <= right; i++ {
        if strings.Contains(vowels, string(words[i][0])) && strings.Contains(vowels, string(words[i][len(words[i])-1])) {
            count++
        }
    }
    return count
}