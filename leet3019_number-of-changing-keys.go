func countKeyChanges(s string) int {
    changes := 0

    for i := 1; i < len(s); i++ {
        if unicode.ToLower(rune(s[i])) != unicode.ToLower(rune(s[i - 1])){
            changes++
        }
    }
    return changes
}