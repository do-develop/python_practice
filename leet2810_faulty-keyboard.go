func finalString(s string) string {
    typed := ""

    for _, c := range s {
        if c == 'i' {
            typed = reverseString(typed)
        } else {
            typed = typed + string(c)
        }
    }
    return typed
}

func reverseString(str string) string {
    runes := []rune(str)

    for i, j := 0, len(str)-1; i < j; i, j = i + 1, j - 1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}