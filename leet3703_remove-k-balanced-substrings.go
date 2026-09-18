func removeSubstring(s string, k int) string {
    var sb strings.Builder
    for range k {
        sb.WriteRune('(')
    }
    for range k {
        sb.WriteRune(')')
    }

    target := sb.String()
    stack := []byte{}

    for i := range s {
        stack = append(stack, s[i])
        for len(stack) >= len(target) && string(stack[len(stack) - len(target):]) == target {
            stack = stack[:len(stack) - len(target)]
        }
    }
    return string(stack)
}