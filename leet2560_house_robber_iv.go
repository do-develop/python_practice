func minCapability(nums []int, k int) int {
    l, r := math.MaxInt32, math.MinInt32
    // set l to min of nums set r to max of nums
    for _, n := range nums {
        if n < l {
            l = n
        }
        if n > r {
            r = n
        }
    }

    // binary search for the min capability
    for l < r {
        mid := (l + r) / 2
        lastVisited, take := false, 0
        for _, n := range nums {
            if lastVisited == true {
                lastVisited = false
                continue
            }
            // greedily check feasibility
            if n <= mid {
                take++
                lastVisited = true
            }
        }
        // binary search on the range of capability
        if take >= k {
            r = mid
        } else {
            l = mid + 1
        }
    }
    return l
}