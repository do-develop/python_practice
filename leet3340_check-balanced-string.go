func isBalanced(num string) bool {
    odd, even := 0, 0

    for i, n := range num {
        digit := int(n - '0')
        if i % 2 == 0 {
            even += digit
        } else {
            odd += digit
        }
    }
    return even == odd
}