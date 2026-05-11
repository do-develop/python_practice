func hasSameDigits(s string) bool {
    N := len(s)
    digits := []byte(s)

    for i := 1; i < N - 1; i++ {
        for j := 0; j < N - i; j++ {
            digits[j] = byte((int(digits[j] - '0') + int(digits[j + 1] - '0')) % 10 + '0')
        }
    }
    return digits[0] == digits[1]
}