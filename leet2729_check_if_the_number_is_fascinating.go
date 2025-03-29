func isFascinating(n int) bool {
    modified := strconv.Itoa(n) + strconv.Itoa(n * 2) + strconv.Itoa(n * 3)

    if len(modified) != 9 {
        return false
    }

    digitCount := make(map[rune]bool)
    for _, digit := range modified {
        if digit == '0' || digitCount[digit] {
            return false
        }
        digitCount[digit] = true
    }
    return len(digitCount) == 9
}