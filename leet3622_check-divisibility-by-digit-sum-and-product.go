func checkDivisibility(n int) bool {
    digitSum := 0
    digitProd := 1
    temp := n

    for temp != 0 {
        digit := temp % 10
        digitSum += digit
        digitProd *= digit
        temp /= 10
    }

    return digitSum != 0 && n % (digitSum + digitProd) == 0
}