func resultingString(s string) string {
    stack := []byte{}

    for i := 0; i < len(s); i++ {
        ch := s[i]

        if len(stack) == 0 {
            stack = append(stack, ch)
        } else {
            if (stack[len(stack)-1] == 'a' && ch == 'z') || (stack[len(stack)-1]== 'z' && ch == 'a') || stack[len(stack)-1] + 1 == ch || stack[len(stack)-1] - 1 == ch{
                stack = stack[:len(stack)-1]
            } else {
                stack = append(stack, ch)
            }
        }
    }
    return string(stack)
}