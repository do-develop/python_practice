func distributeCandies(n int, limit int) int {
    var count int
    for i := 0; i <= min(limit, n); i++ {
        for j := 0; j <= min(limit, n - i); j++ {
            if n - i - j <= limit {
                count++
            }
        }
    }
    return count
}