func minCuttingCost(n int, m int, k int) int64 {
    if n <= k && m <= k {
        return 0
    }

    res := 0
    if n > k {
        res += k * (n - k)
    }
    if m > k {
        res += k * (m - k)
    }

    return int64(res)
}