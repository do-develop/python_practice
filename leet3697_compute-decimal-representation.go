func decimalRepresentation(n int) []int {
    res := make([]int, 0, 10)
    pow := 1

    for n > 0 {
        if n % 10 != 0 {
            res = append(res, n % 10 * pow)
        }
        pow *= 10
        n /= 10
    }
    slices.Reverse(res)
    return res
}