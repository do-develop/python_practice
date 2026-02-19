func reportSpam(message []string, bannedWords []string) bool {
    set := map[string]bool {}

    for i := range bannedWords {
        set[bannedWords[i]] = true
    }

    count := 0
    for _, msg := range message {
        if set[msg] {
            count++
        }
        if count == 2 {
            return true
        }
    }
    return false
}