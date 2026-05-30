func minCosts(cost []int) []int {
    N := len(cost)
    ans := make([]int, N)
    price := cost[0]

    for i := 0; i < N; i++ {
        if cost[i] < price {
            price = cost[i]
        }
        ans[i] = price
    }
    return ans
}