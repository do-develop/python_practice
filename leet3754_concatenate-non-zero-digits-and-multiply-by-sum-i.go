func sumAndMultiply(n int) int64 {
    var x int64 = 0
    var digitSum int64 = 0

    s := strconv.Itoa(n)
    for _,c := range s {
        digit := int64(c - '0')
        digitSum += digit
        if digit > 0 {
            x = x * 10 + digit
        }
    }
    return x * digitSum
}