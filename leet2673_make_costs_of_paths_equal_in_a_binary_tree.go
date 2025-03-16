func minIncrements(n int, cost []int) int {
    res := 0
    for i := n/2 - 1; i >= 0; i-- {
        l, r := i * 2 + 1, i * 2 + 2
        res += int(math.Abs(float64(cost[l] - cost[r])))
        cost[i] += max(cost[l], cost[r])
    }
    return res
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}