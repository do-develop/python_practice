func maxProduct(n int) int {
    digits := []int{}
    for n > 0 {
        digits = append(digits, n % 10)
        n = n / 10
    }

    sort.Ints(digits)
    return digits[len(digits) - 2] * digits[len(digits) - 1]
}