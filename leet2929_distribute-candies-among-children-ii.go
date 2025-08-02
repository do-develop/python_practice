func distributeCandies(n int, limit int) int64 {
    ways := int64(0)

    for x := 0; x <= min(limit, n); x++ {
        if n - x > 2 * limit { // no valid distribution way
            continue 
        }
        ways += int64(min(n - x, limit) - max(0, n - x - limit) + 1)
    }
    return ways
}