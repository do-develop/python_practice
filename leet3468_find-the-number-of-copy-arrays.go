func countArrays(original []int, bounds [][]int) int {
    lo, hi := math.MinInt64, math.MaxInt64

    for i := 0; i < len(original); i++ {
        diff := original[i] - original[0]

        lo = max(lo, bounds[i][0] - diff)
        hi = min(hi, bounds[i][1] - diff)
    }

    if lo > hi {
        return 0
    }

   return hi - lo + 1
}