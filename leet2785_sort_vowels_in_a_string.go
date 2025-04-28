func isVowel(char byte) bool {
    vowels := "aeiouAEIOU"
    return strings.ContainsRune(vowels, rune(char))
}

func sortVowels(s string) string {
    bytes := []byte(s)
    vowels := make([]byte, 0)

    for i:= 0; i < len(bytes); i++ {
        if isVowel(bytes[i]) {
            vowels = append(vowels, bytes[i])
        }
    }

    sort.Slice(vowels, func(i, j int) bool {
        return vowels[i] < vowels[j]
    })

    pos := 0
    for i := 0; i < len(bytes); i++ {
        if isVowel(bytes[i]) {
            bytes[i] = vowels[pos]
            pos++
        }
    }
    return string(bytes)
}
