func generateTag(caption string) string {
    var builder strings.Builder
    words := strings.Fields(caption)
    if len(words) == 0 {
        return "#"
    }

    builder.WriteRune('#')
    builder.WriteString(strings.ToLower(words[0]))

    for _, w := range words[1:] {
        builder.WriteString(strings.ToUpper(w[:1]))
        builder.WriteString(strings.ToLower(w[1:]))
    }

    ans := builder.String()
    if len(ans) > 100 {
        return ans[:100]
    }
    return ans
}