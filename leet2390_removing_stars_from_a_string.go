func removeStars(s string) string {
    // use stack and pop if meets *
    var stack []byte

    for i:=0; i<len(s); i++ {
        if s[i] == '*' {
            stack = stack[:len(stack) - 1]
        } else {
            stack = append(stack, s[i])
        }
    }
    return string(stack)
}