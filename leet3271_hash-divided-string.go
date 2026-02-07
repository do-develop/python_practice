func stringHash(s string, k int) string {
    var strBuilder strings.Builder
    for i := 0; i + k <= len(s); i += k {
        strBuilder.WriteRune(strHash(s[i:i+k]))
    }
    return strBuilder.String()
}

func strHash(s string) rune {
    sum := 0
    for _, r := range s {
        sum += int(r - 'a')
    }
    return rune(sum % 26 + 'a')
}