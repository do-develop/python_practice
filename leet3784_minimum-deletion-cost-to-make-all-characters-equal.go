func minCost(s string, cost []int) int64 {
    var totalCost int64
    var costPerChar [26]int64
    var maxCost int64 = 0

    for i := 0; i < len(cost); i++ {
        c := int64(cost[i])
        totalCost += c

        pos := s[i] - 'a'
        costPerChar[pos] += c

        if costPerChar[pos] > maxCost {
            maxCost = costPerChar[pos]
        }
    }

    return totalCost - maxCost
}