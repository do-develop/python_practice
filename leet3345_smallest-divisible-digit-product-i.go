func smallestNumber(n int, t int) int {
    for getProduct(n) % t != 0 {
        n++
    }
    return n
}

func getProduct(num int) int {
    prod := 1
    for num > 0 {
        prod *= num % 10
        num /= 10
    }
    return prod
}