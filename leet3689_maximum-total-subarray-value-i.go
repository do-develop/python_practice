func maxTotalValue(nums []int, k int) int64 {
    mini, maxi := math.MaxInt, math.MinInt

    for _, n := range nums {
        mini = min(mini, n)
        maxi = max(maxi, n)
    }

    return int64(maxi - mini) * int64(k)
}