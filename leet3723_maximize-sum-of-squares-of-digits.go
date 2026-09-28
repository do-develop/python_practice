func maxSumOfSquares(num int, sum int) string {
    if sum > num * 9 {
        return ""
    }

    res := make([]byte, num)
    for i := range res {
        digit := min(sum, 9)
        res[i] = byte(digit) + '0'
        sum -= digit
    }
    return string(res)
}