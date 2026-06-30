func maxSumDistinctTriplet(x []int, y []int) int {
    // For each distinct x, keep only the max y
    bestY := make(map[int]int)
    for i, xi := range x {
        if curr, exists := bestY[xi]; !exists || y[i] > curr {
            bestY[xi] = y[i]
        }
    }

    if len(bestY) < 3 {
        return -1
    }

    vals := make([]int, 0, len(bestY))
    for _, v := range bestY {
        vals = append(vals, v)
    }

    N := len(vals)
    sort.Ints(vals)
    return vals[N-1] + vals[N-2] + vals[N-3]
}