func splitNum(num int) int {
    digits := make([]int, 10)
    for num > 0 {
        digits[num%10]++
        num /= 10
    }
    n1, n2 := 0, 0
    odd := true
    for i := 0; i < 10; i++ {
        for digits[i] > 0 {
            if odd {
                n1 = n1 * 10 + i
            } else {
                n2 = n2 * 10 + i
            }
            digits[i]--
            odd = !odd
        }
    }
    return n1 + n2
}