func minCost(nums []int, x int) int64 {
    N := len(nums)
    res := make([]int, N)

    // To store cumulative cost for different shift values k
    for k := 0; k < N; k++ {
        res[k] = x * k
    }

    for i := 0; i < N; i++ {
        cur := nums[i]
        for k := 0; k < N; k++ {
            //keep minimum cost encountered in the last k shifts
            cur = int(math.Min(float64(cur), float64(nums[(i - k + N) % N])))
            res[k] += cur
        }
    }

    // find the min value in res
    miniCost := math.MaxInt64
    for _, val := range res {
        if val < miniCost {
            miniCost = val
        }
    }
    return int64(miniCost)
}