func differenceOfSums(n int, m int) int {
    diff := 0
    for i := 1; i <= n; i++ {
        if i % m == 0 {
            diff -= i
        } else {
            diff += i
        }
    }
    return diff
}