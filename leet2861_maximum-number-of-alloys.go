func maxNumberOfAlloys(n int, k int, budget int, composition [][]int, stock []int, cost []int) int {
    maxPossible := slices.Min(stock) + budget // set upper bound, loose ceiling for binary search
	maxAlloys := 0

    // find the max number of alloys that can be made from each composition separately, then sum them up.
    for _, comp := range composition {
        maxAlloys += sort.Search(maxPossible - maxAlloys, func(i int) bool {
            // find first i that goes over budget and subtract 1 == max number of alloy can be made
            target := maxAlloys + i + 1 
            totalCost := 0

            // loop over each type of metal
            for j := 0; j < n; j++ {
                required := comp[j] * target
                if required > stock[j] {
                    totalCost += (required - stock[j]) * cost[j]
                    if totalCost > budget {
                        return true
                    }
                }
            }
            return false
        })
    }
    return maxAlloys
}