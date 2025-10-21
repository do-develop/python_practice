func isSubstringPresent(s string) bool {
    string := []rune(s)

    for i := len(string) - 1; i > 0; i-- {
        substr := fmt.Sprintf("%c%c", string[i], string[i - 1])
        isPresent := strings.Contains(s, substr)
        if isPresent {
            return true
        }
    }
    return false
}