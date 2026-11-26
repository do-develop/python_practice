func minimumCost(cost1 int, cost2 int, costBoth int, need1 int, need2 int) int64 {
    var totalCost int64 = 0

    if cost1 + cost2 <= costBoth {
        totalCost = int64(cost1) * int64(need1) + int64(cost2) * int64(need2)
    } else {
        count3 := min(need1, need2)
        totalCost = int64(count3) * int64(costBoth)

        need1 -= count3
        need2 -= count3

        if need1 > 0 {
            totalCost += int64(need1) * int64(min(cost1, costBoth))
        } else if need2 > 0 {
            totalCost += int64(need2) * int64(min(cost2, costBoth))
        }
    }
    return totalCost
}